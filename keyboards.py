from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔁 Хочу обменять", callback_data="exchange")],
        [InlineKeyboardButton(text="💰 Хочу сдать", callback_data="sell")]
    ])

def models_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="iPhone 12", callback_data="m_12")],
        [InlineKeyboardButton(text="iPhone 13", callback_data="m_13")],
        [InlineKeyboardButton(text="iPhone 14", callback_data="m_14")],
        [InlineKeyboardButton(text="iPhone 15", callback_data="m_15")]
    ])

def screen_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="идеальный", callback_data="screen_perfect")],
        [InlineKeyboardButton(text="царапины", callback_data="screen_scratches")],
        [InlineKeyboardButton(text="трещины", callback_data="screen_cracked")],
        [InlineKeyboardButton(text="разбит", callback_data="screen_broken")]
    ])

def body_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="идеал", callback_data="body_perfect")],
        [InlineKeyboardButton(text="следы", callback_data="body_light")],
        [InlineKeyboardButton(text="сильные повреждения", callback_data="body_heavy")]
    ])

def repair_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="нет", callback_data="repair_no")],
        [InlineKeyboardButton(text="был ремонт", callback_data="repair_yes")],
        [InlineKeyboardButton(text="вода", callback_data="repair_water")]
    ])