import telebot
from telebot import types
import requests
import time
import os
import colorama
from tonapi import Tonapi

from tonapi.utils import nano_to_amount
from colorama import Fore, Back, Style


token = "6082223551:AAGRRYlNgIzgWwoCUYTC-2p_jOT--3u-po8"
channel_id = "@ctktonapi"
bot = telebot.TeleBot(token)
bot_status = 0



os.system('CLS')
print(Fore.GREEN + '' + "\n" +
      '██╗      ██████╗  ██████╗  ██████╗ ██╗███╗   ██╗ ██████╗ ' + "\n" +
      '██║     ██╔═══██╗██╔════╝ ██╔════╝ ██║████╗  ██║██╔════╝ ' + "\n" +
      '██║     ██║   ██║██║  ███╗██║  ███╗██║██╔██╗ ██║██║  ███╗' + "\n" +
      '██║     ██║   ██║██║   ██║██║   ██║██║██║╚██╗██║██║   ██║' + "\n" +
      '███████╗╚██████╔╝╚██████╔╝╚██████╔╝██║██║ ╚████║╚██████╔╝' + "\n" +
      '╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ' + "\n" 
      )


@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == "/postupdate":
        print(Fore.GREEN + f'Пользователь воспользовался командой /postupdate')
        bot_status = 1
    else:
        bot_status = 0
        print(Fore.RED + f'Кто-то ввел неизвестную команду')
        bot.send_message(message.from_user.id, "Команда не найдена или у вас нет прав для её использования.")
    while bot_status == 1:
        tonapi = Tonapi(api_key="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiY290aWt5dCJdLCJleHAiOjE4MzQ5MzU4MjAsImlzcyI6IkB0b25hcGlfYm90IiwianRpIjoiU0FTUDNOVlVIMk40QzU1TFVRQ0pNQUtJIiwic2NvcGUiOiJzZXJ2ZXIiLCJzdWIiOiJ0b25hcGkifQ.tOMNvXqWmOfVjkaWmDyMjqFS4tqfe_1PkZmH2T8x3O_timRDVRVp5fy1gT8bOiBQSWS7-rqXiNFCTz71fitlAw")
        address = "EQCsrZwuaFWa68Ci-IR3VqFs4I03vmbFSdbX42hkngZRH7s4"
        account = tonapi.account.get_info(account=address)
        balance = nano_to_amount(account.balance)

        price = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym=TONCOIN&tsyms=RUB"
        ).json()
        form01 = (
            "{}₽"
                ).format(
                    round(price["RUB"] * 0.1 - 1),
                )
        form1 = (
            "{}₽"
                ).format(
                    round(price["RUB"] - 10),
                )
        price_01 = form01
        price_1 = form1

        msg1 = 'Продаю тон:' + "\n" + f'Баланс: {balance} TON' + "\n" + f'Цена: 0.1 TON = {price_01}' + "\n" + f'Цена: 0.1 TON = {price_1}'
        msg2 = 'Продаю тон:' + "\n" + f'Баланс: {balance} ТON' + "\n" + f'Цена: 0.1 TON = {price_01}' + "\n" + f'Цена: 0.1 TON = {price_1}'

        bot.edit_message_text(f'{msg2}', chat_id=channel_id, message_id=5)
        bot.edit_message_text(f'{msg1}', chat_id=channel_id, message_id=5)
        
        print(Fore.CYAN + 'Пост был обновлен!' + "\n" + 
            f'Баланс: {balance}' + "\n" +
            f'Цена за 0.1 TON: {price_01}' + "\n" +
            f'Цена за 1 TON: {price_1}'
            )
        bot.send_message(message.from_user.id, "Пост обновлен!")
        bot_status = 0
    print("\n")

  

bot.polling()