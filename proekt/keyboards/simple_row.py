# В этом файле идет создание самой простой клавиатуры
# :param items: список текстов для кнопок
# :return: объект реплай-клавиатуры
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_bot = ["Расчитать ежемесячный платеж", "Расчитать ипотечный платеж", "Досрочное погашение кредита"]
kb_ipoteka = ["Да", "Нет"]

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
