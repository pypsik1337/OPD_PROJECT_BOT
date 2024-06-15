from aiogram.filters import Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.simple_row import make_row_keyboard
from keyboards.simple_row import kb_bot

loan_early_credit_router = Router()


class loan_ecredit(StatesGroup):
    sum_ecredit = State()
    procent_ecredit = State()
    term_ecredit =State()
    early_summ = State()
    early_term = State()

@loan_early_credit_router.message(Command("e_credit"))
@loan_early_credit_router.message(F.text.lower() == "досрочное погашение кредита")
async def cmd_sum_ecredit(message: Message, state: FSMContext):
    await message.answer("Расчет ежемесячного платежа, по кредите с досрочным погашением. Введите сумму вашего кредита: ", reply_markup= ReplyKeyboardRemove())
    await state.set_state(loan_ecredit.sum_ecredit)
    
@loan_early_credit_router.message(loan_ecredit.sum_ecredit)
async def cmd_procent_ecredit(message:Message, state: FSMContext):
    try:
        await state.update_data(chosen_ecredit_sum = float(message.text))
        await message.answer("Теперь, введите процент кредитования.")
        await state.set_state(loan_ecredit.procent_ecredit)
    except Exception: 
        await message.answer("Вы ввели не число!")

@loan_early_credit_router.message(loan_ecredit.procent_ecredit)
async def cmd_term_ecredit(message:Message, state: FSMContext):
    try:
        await state.update_data(chosen_procent_ecredit = float(message.text))
        await message.answer("Теперь введите срок на который оформлялся кредит(в месяцах)")
        await state.set_state(loan_ecredit.term_ecredit)
    except Exception:
        await message.answer("Вы ввели не число!")
        
@loan_early_credit_router.message(loan_ecredit.term_ecredit)
async def cmd_sum_e(message: Message, state: FSMContext):
    try:
        await state.update_data(chosen_term = int(message.text))
        await message.answer("Теперь, введите сумму которые хотите внести для дросрочного погашения кредита")
        await state.set_state(loan_ecredit.early_summ)
    except Exception:
        await message.answer("Вы ввели не число!")
        
@loan_early_credit_router.message(loan_ecredit.early_summ)
async def cmd_term_e(message: Message, state: FSMContext):
    try:
        await state.update_data(chosen_esum = float(message.text))
        await message.answer("Хорошо, теперь, введите месяц в который будет внесен досрочный платеж")
        await state.set_state(loan_ecredit.early_term)
    except Exception:
        await message.answer("Вы ввели не число!")
        
@loan_early_credit_router.message(loan_ecredit.early_term)
async def cmd_finaly_ecredit(message: Message, state: FSMContext):
    try:
        await state.update_data(chosen_eterm = float(message.text))
        user_data = await state.get_data()
        months_rate = user_data["chosen_procent_ecredit"]/100/12
        d_rate = user_data["chosen_esum"]
        d_month = user_data['chosen_eterm']
        sum_credit = user_data["chosen_ecredit_sum"]
        months = user_data["chosen_term"]
        months_pay = (sum_credit * months_rate) / (1- (1+months_rate) ** -months)
        total_sum_credit = months_pay * months
        OD_sum = months_pay *(d_month)
        dosrok_ostat_sum = sum_credit - OD_sum
        
        dp_sum_credit = dosrok_ostat_sum - d_rate
        
        dp_months_pay = (dp_sum_credit * months_rate) / (1- (1+months_rate) ** -(months-d_month))
        await message.answer(f"Сумма вашего кредита равна: {user_data["chosen_ecredit_sum"]}руб.\n" 
                             f"Процент: {user_data['chosen_procent_ecredit']}% годовых.\n"
                             f"Срок: {user_data['chosen_term']} мес.\n"
                             f"Общая сумма выплат составит: {round(total_sum_credit, 2)} руб\n"
                             f"Ежемесячный платеж составит: {round(months_pay,2)} руб."
                             f"Если вы внесете {round(user_data['chosen_esum'], 2)} руб., на {user_data['chosen_eterm']} месяце платежа.\n"
                             f"Ежемесячный платеж составит: {round(dp_months_pay, 2)}", 
                             reply_markup=make_row_keyboard(kb_bot))
        await state.clear()
    except Exception:
        await message.answer("Вы ввели не число!")