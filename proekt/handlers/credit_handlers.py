from aiogram.filters import Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.simple_row import make_row_keyboard
from keyboards.simple_row import kb_bot

loan_credit_router = Router() 

class loan_calculation(StatesGroup):
    sum = State()
    procent = State()
    term = State()
    
@loan_credit_router.message(Command("go_credit"))
@loan_credit_router.message(F.text.lower() == "расчитать ежемесячный платеж")
async def cmd_sum(message: Message, state: FSMContext):
    await message.answer("Расчет ежемесячного процента по кредиту, введите сумму которую хотите взять", reply_markup= ReplyKeyboardRemove())
    await state.set_state(loan_calculation.sum)


@loan_credit_router.message(loan_calculation.sum,)
async def cmd_procent(message:Message, state: FSMContext):
    try:
        await state.update_data(chosen_sum = int(message.text))
        await message.answer("Теперь, введите процент кредитования.")
        await state.set_state(loan_calculation.procent)
    except Exception: 
        await message.answer("Вы ввели не число!")
    
@loan_credit_router.message(loan_calculation.procent)
async def cmd_term(message:Message, state: FSMContext):
    try:
        await state.update_data(chosen_procent = int(message.text))
        await message.answer("Теперь введите срок на который оформляется кредит(в месяцах)")
        await state.set_state(loan_calculation.term)
    except Exception:
        await message.answer("Вы ввели не число!")
        
    
@loan_credit_router.message(loan_calculation.term)
async def cmd_final_loan(message: Message, state: FSMContext):
    try:        
        await state.update_data(chosen_term = int(message.text))
        user_data = await state.get_data()
        months_rate = user_data["chosen_procent"]/100/12
        sum_credit = user_data["chosen_sum"]
        months = user_data["chosen_term"]
        months_pay = (sum_credit * months_rate) / (1- (1+months_rate) ** -months)
        total_sum_credit = months_pay * months
        await message.answer(f"Сумма вашего кредита равна: {user_data['chosen_sum']}руб.\n" 
                             f"Процент: {user_data['chosen_procent']}% годовых.\n"
                             f"Срок: {user_data['chosen_term']} мес.\n"
                             f"Общая сумма выплат составит: {round(total_sum_credit, 2)} руб\n"
                             f"Ежемесячный платеж составит: {round(months_pay,2)} руб.", 
                             reply_markup=make_row_keyboard(kb_bot))
        await state.clear()
    except Exception:
        await message.answer("Вы ввели не число!")