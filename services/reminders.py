import asyncio

async def reminder(bot, user_id, text, delay):
    await asyncio.sleep(delay)
    try:
        await bot.send_message(user_id, text)
    except:
        pass


async def schedule(bot, user_id, model, price):
    asyncio.create_task(
        reminder(bot, user_id,
                 f"👋 Напоминание: ваше предложение {model} — {price} ₽",
                 60*30)
    )

    asyncio.create_task(
        reminder(bot, user_id,
                 f"⚡ Всё ещё актуально: {price} ₽ за ваш iPhone",
                 60*60*3)
    )

    asyncio.create_task(
        reminder(bot, user_id,
                 f"📱 Последнее напоминание — {price} ₽ всё ещё доступно",
                 60*60*24)
    )