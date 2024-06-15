# from aiogram.filters import Command, CommandStart, StateFilter
# from aiogram import types, Router, F
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import Message, ReplyKeyboardRemove

# from keyboards.simple_row import make_row_keyboard, make_kb_ipoteka


# credit_router = Router()

# kb_bot = ["Расчитать ежемесячный платеж", "Расчитать ипотечный платеж", "Досрочное погашение кредита"]
# kb_ipoteka = ["Да", "Нет"]

# class RCredit(StatesGroup):
#     credit_func = State()
#     ipoteka_func = State()
#     scredit_func = State()
    
    
    
    
# @credit_router.message(Command("credit"))
# @credit_router.message(F.text.lower() == "расчитать ежемесячный платеж")
# async def precalcualte(message: types.Message, state: FSMContext):
#     await message.answer("Отправьте мне сумму кредита, процентную ставку и срок в месяцах через запятую")
#     await state.set_state(RCredit.credit_func)
    
    
# @credit_router.message(RCredit.credit_func)
# async def calcualte(message:Message, state: FSMContext):
#     try:
#         sum_credit, interest_rate, months = map(float, message.text.split(","))
#         months_rate = interest_rate/100/12
#         months_pay = (sum_credit * months_rate) / (1- (1+months_rate) ** -months)
#         total_sum_credit = months_pay * months
#         await message.answer(f"Ваш ежемесячный платеж составит: {round(months_pay,2)} руб.\nСумма всего платежа составит: {round(total_sum_credit,2)}",
                             
#                              reply_markup=make_row_keyboard(kb_bot),resize_keyboard=True
#                                 )
#     except Exception as e:
#         await message.answer("Вы ввели некорректные данные")
    
#     await state.clear()
    
# @credit_router.message(Command("ipoteka"))
# @credit_router.message(F.text.lower() == "расчитать ипотечный платеж")
# async def cmd_ipoteka(message: Message, state: FSMContext):
#     await message.answer("Вы хотите взять ипотеку?", reply_markup=make_kb_ipoteka(kb_ipoteka))
#     await state.set_state(RCredit.ipoteka_func)
    
# # Тут хендлеры на ипотеку
    
# @credit_router.message(F.text == "Да")
# async def cmd_ipoteka_yes(message: Message, state: FSMContext):
#     await message.answer("Сочувствую!", reply_markup= make_row_keyboard(kb_bot))
#     await state.clear()

# @credit_router.message(F.text == "Нет")
# async def cmd_ipoteka_no(message: Message, state: FSMContext):
#     await message.answer("МЕГАХОРОШ!", reply_markup= make_row_keyboard(kb_bot))
#     await state.clear()
    
# # Тут хендлеры на досрочное погашение

# @credit_router.message(Command("scredit"))
# @credit_router.message(F.text.lower() == "досрочное погашение кредита")
# async def cmd_scredit(message: Message, state: FSMContext):
#     await message.answer("Введите сумму кредита, процентную ставку, срок платежа, сумму платежа для досрочного погашения, месяц платежа через запятую!")
#     await state.set_state(RCredit.scredit_func)

# @credit_router.message(RCredit.scredit_func)
# async def scredit_r(message:Message, state: FSMContext):
#     try:
#         sum_credit, interest_rate, months, d_rate, d_month = map(float, message.text.split(","))
    
#         months_rate = interest_rate/100/12
#         months_pay = (sum_credit * months_rate) / (1- (1+months_rate) ** -months)
#         total_sum_credit = months_pay * months
#         dp_sum_credit = sum_credit - d_rate
#         dp_months_pay = (dp_sum_credit * months_rate) / (1- (1+months_rate) ** -(months-d_month))
     
#         await message.answer(f"Ваш ежемемесячный платеж составит: {round(months_pay,2)} руб \n"
#                          f"Сумма всего платежа составит: {round(total_sum_credit,2)}\n"
#                          f"Если вы внесете {d_rate} руб для досрочного покашения кредита на {int(d_month)} месяце платежа\n"
#                          f"Ежемесячный платеж станет: {round(dp_months_pay, 2)} руб.",
#                          reply_markup=make_row_keyboard(kb_bot))
#     except Exception as e:
#         await message.answer("Вы ввели некорректные данные")
                                                     
                                                     
    
    

    