from aiogram.filters import Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.simple_row import make_row_keyboard
from keyboards.simple_row import kb_bot

class loan_morgage(StatesGroup):
    chose_sum_morgage = State()
    chose_procent_morgage =State()
    chose_term_morgage = State()
    chose_down_payment = State()
    
    
loan_morgage_router = Router()

@loan_morgage_router.message(Command("morgage"))
@loan_morgage_router.message(F.text.lower() == "расчитать ипотечный платеж")
async def cmd_sum_morgage(messsage: Message, state:FSMContext):
    await messsage.answer("Расчет ипотечного кредитования с первоначальным взносом.\nВведите сумму ипотеки: ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(loan_morgage.chose_sum_morgage)

@loan_morgage_router.message(loan_morgage.chose_sum_morgage)
async def cmd_procent_morgage(message: Message, state: FSMContext):
    try:
        await state.update_data(chosen_morgage_sum = float(message.text))
        await message.answer("Теперь введите процент ставки по ипотеке")
        await state.set_state(loan_morgage.chose_procent_morgage)
    except Exception: 
        await message.answer("Вы ввели не число!")
        
@loan_morgage_router.message(loan_morgage.chose_procent_morgage)
async def cmd_term_morgage(message:Message, state: FSMContext):
    try:
        await state.update_data(chosen_morgage_rate = float(message.text))
        await message.answer("Теперь, введите на сколько лет берется ипотека.")
        await state.set_state(loan_morgage.chose_term_morgage)
    except Exception: 
        await message.answer("Вы ввели не число!")
    
@loan_morgage_router.message(loan_morgage.chose_term_morgage)
async def cmd_downpay_morgage(message:Message, state:FSMContext):
    try:
        await state.update_data(chose_moragage_years = float(message.text))
        await message.answer("Хорошо, теперь, введите ваш первоначальный взнос")
        await state.set_state(loan_morgage.chose_down_payment)
    except Exception: 
        await message.answer("Вы ввели не число!")
    
@loan_morgage_router.message(loan_morgage.chose_down_payment)
async def cmd_morgage(message:Message, state:FSMContext):
    try:
        await state.update_data(chose_moragage_down = float(message.text))
        user_data = await state.get_data()
        principal = user_data['chosen_morgage_sum']
        down_payment = user_data["chose_moragage_down"]
        annual_interest_rate = user_data["chosen_morgage_rate"]
        years = user_data["chose_moragage_years"]
        # Сумма кредита после первоначального вклада
        loan_amount = principal - down_payment
        # Месячная процентная ставка
        monthly_interest_rate = annual_interest_rate / 12 / 100
        # Общее количество месячных платежей
        number_of_payments = years * 12
        # Формула для расчета ежемесячного платежа
        monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) /((1 + monthly_interest_rate) ** number_of_payments - 1)
        await message.answer(f"Ваш ежемесячный платеж по ипотеке составит: {round(monthly_payment,2)} руб.",
                             reply_markup=make_row_keyboard(kb_bot)
                             )          
        await state.clear()
    except Exception as e: 
        await message.answer(e)
        await message.answer("Что то пошло не так")

