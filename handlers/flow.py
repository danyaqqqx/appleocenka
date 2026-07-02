from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states import Form
from keyboards import *
from services.calculator import get_price
from services.notifier import notify_admin
from services.reminders import schedule
from storage import USERS

router = Router()


@router.message(F.text == "/start")
async def start(m: Message, state: FSMContext):
    await state.set_state(Form.action)
    await m.answer(
        "Привет 👋\nВыбери действие:",
        reply_markup=start_kb()
    )


@router.callback_query(F.data.in_(["exchange", "sell"]))
async def action(c: CallbackQuery, state: FSMContext):
    USERS[c.from_user.id] = {}
    USERS[c.from_user.id]["action"] = c.data

    await state.set_state(Form.user_model)
    await c.message.answer("Выбери модель iPhone:", reply_markup=models_kb())


@router.callback_query(F.data.startswith("m_"))
async def model(c: CallbackQuery, state: FSMContext):
    USERS[c.from_user.id]["model"] = c.data.split("_")[1]

    await state.set_state(Form.screen)
    await c.message.answer("Состояние экрана:", reply_markup=screen_kb())


@router.callback_query(F.data.startswith("screen_"))
async def screen(c: CallbackQuery, state: FSMContext):
    USERS[c.from_user.id]["screen"] = c.data

    await state.set_state(Form.battery)
    await c.message.answer("Введите точный % батареи (0-100):")


@router.message(Form.battery)
async def battery(m: Message, state: FSMContext):
    USERS[m.from_user.id]["battery"] = int(m.text)

    await state.set_state(Form.body)
    await m.answer("Состояние корпуса:", reply_markup=body_kb())


@router.callback_query(F.data.startswith("body_"))
async def body(c: CallbackQuery, state: FSMContext):
    USERS[c.from_user.id]["body"] = c.data

    await state.set_state(Form.repair)
    await c.message.answer("Был ли ремонт?", reply_markup=repair_kb())


@router.callback_query(F.data.startswith("repair_"))
async def repair(c: CallbackQuery, state: FSMContext):
    USERS[c.from_user.id]["repair"] = c.data

    data = USERS[c.from_user.id]

    price = get_price(data)
    data["price"] = price

    extra = 15000 if data["action"] == "exchange" else 0
    data["extra"] = extra
    data["user_id"] = c.from_user.id
    data["username"] = c.from_user.username or "no_username"

    await c.message.answer(
        f"📊 Оценка готова\n💰 {price} ₽\n🔁 Доплата: {extra} ₽"
    )

    await notify_admin(c.bot, data)
    await schedule(c.bot, c.from_user.id, data["model"], price)

    await state.clear()