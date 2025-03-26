from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

startMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💵 Курс'),
            KeyboardButton(text='➡️ Меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    is_persistent=True,
    input_field_placeholder='Начальное меню'
)

subMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💹 Прайс'),
            KeyboardButton(text='🚹 Информация'),
            KeyboardButton(text='☎️ Связь')
        ],
        [
            KeyboardButton(text='⬅️ Назад')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Подменю'
)

urlsMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔗 Перейти в чат', url='https://t.me/+kGuIffS3xedmYzYy')

        ]
    ]
)