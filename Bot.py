from aiogram import Bot, Dispatcher, executor, types
from ai.llm import ask_llm
from faiss_index import search_context

bot = Bot(token="7655639090:AAHaovZK8kjPcxwCYsbEO4HByxodvFIgYH0")
dp = Dispatcher(bot)

@dp.message_handler()
async def answer(msg: types.Message):
    context = search_context(msg.text)
    answer = ask_llm(context, msg.text)
    await msg.answer(answer)

executor.start_polling(bot)
