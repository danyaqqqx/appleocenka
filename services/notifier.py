from config import ADMIN_CHAT_ID

async def notify_admin(bot, data):
    text = f"""
📱 НОВАЯ ЗАЯВКА

Тип: {data['action']}
Модель: {data['model']}
Хочет: {data.get('target_model','-')}

Экран: {data['screen']}
Батарея: {data['battery']}%
Корпус: {data['body']}
Ремонт: {data['repair']}

💰 Цена: {data['price']} ₽
🔁 Доплата: {data.get('extra', 0)} ₽

👤 @{data['username']}
ID: {data['user_id']}
"""
    await bot.send_message(ADMIN_CHAT_ID, text)