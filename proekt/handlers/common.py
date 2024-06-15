from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.simple_row import  make_row_keyboard
from handlers.credit_handlers import kb_bot

common_router = Router()

@common_router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Привет! Я Бот Нелепый. Расчитаю тебе платеж по кредиту ",
                         reply_markup= make_row_keyboard(kb_bot)
                        )

@common_router.message(StateFilter(None), Command(commands="cancel"))
@common_router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(
        text="Нечего отменять", reply_markup= make_row_keyboard(kb_bot)
        
    )
    

@common_router.message(Command(commands="cancel"))
@common_router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Действие отменено", reply_markup=make_row_keyboard(kb_bot))