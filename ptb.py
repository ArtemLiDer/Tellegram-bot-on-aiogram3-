from aiogram import Bot, Dispatcher, Router, types
import requests
import datetime
import logging
import asyncio
import sys
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

API_TOKEN = '6541378570:AAGiu4u35QAUYFp8Wh8xtWEQop8em_wiQUM'
open_weather_token = "e608ed9968bf7e78a20eee2a3e3fc092"

dp = Dispatcher()
async def on_startap():
    print('online')

@dp.message(CommandStart())
async def start_weather_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def reg_weather_handler(message:  types.Message):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F328"
    }


    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()


        city = data['name']
        cur_weather = data['main']['temp']


        weather_pogoda= data['weather'][0]['main']
        if weather_pogoda in code_to_smile:
            wb = code_to_smile[weather_pogoda]
        else:
            print('Смотри сам')



        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sun = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        nicht = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenhth_of_the_day= datetime.datetime.fromtimestamp(data['sys']['sunrise']) - datetime.datetime.fromtimestamp(
            data['sys']['sunset'])



        await message.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература:{cur_weather}C° {wb}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\n"
              f"Скорость ветра: {wind} м\с\nЗакат: {sun}\n"
              f"Восход: {nicht}\nВремя между восходом и закатам {lenhth_of_the_day}")


    except:
        await message.answer("\U00002620Проверти название города!\U00002620")


async def main():
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, on_startap=on_startap)




if __name__ =="__main__":    
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,)
    asyncio.run(main())



 