from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_bot = ["Расчитать ежемесячный платеж", "Расчитать ипотечный платеж", "Досрочное погашение кредита"]
kb_ipoteka = ["Да", "Нет"]

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
