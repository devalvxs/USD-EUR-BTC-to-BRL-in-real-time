

from colorama import init, Fore, Back

init ()

import requests
import json
from time import sleep
from colorama import Fore

moeda = input(Fore.LIGHTRED_EX + "Qual moeda deseja converter em reais (USD/EUR/BTC)?: ").upper()

while moeda not in ["USD", "EUR", "BTC"]:
    moeda = input(Fore.LIGHTRED_EX + "Qual moeda deseja converter em reais (USD/EUR/BTC)?: ").upper()
    if moeda not in ["USD", "EUR", "BTC"]:
        print(Fore.RED + "Moeda não encontrada ou inválida:", moeda)
        print(Fore.LIGHTRED_EX + "EX: USD, EUR, BTC...")

while True:

    response = requests.get("https://economia.awesomeapi.com.br/json/last/" + moeda)
    cotacao = json.loads(response.text)

    print(Fore.GREEN+"Moeda inserida:", moeda)

    if moeda == "USD" and "USDBRL" in cotacao:
        baixo = round(float(cotacao["USDBRL"]["low"]), 2)
        alto = round(float(cotacao["USDBRL"]["high"]), 2)

        print(Fore.YELLOW + "Moeda: " + cotacao["USDBRL"]["name"])
        print(Fore.CYAN + "Valor mais alto do Dolar: R$" + str(alto))
        print(Fore.CYAN + "Valor mais baixo do Dolar: R$" + str(baixo))
        print("----------------")

    elif moeda == "EUR" and "EURBRL" in cotacao:
        baixo = round(float(cotacao["EURBRL"]["low"]), 2)
        alto = round(float(cotacao["EURBRL"]["high"]), 2)

        print(Fore.YELLOW + "Moeda: " + cotacao["EURBRL"]["name"])
        print(Fore.CYAN + "Valor mais alto do Euro: R$" + str(alto))
        print(Fore.CYAN + "Valor mais baixo do Euro: R$" + str(baixo))
        print("----------------")

    elif moeda == "BTC" and "BTCBRL" in cotacao:
        baixo = round(float(cotacao["BTCBRL"]["low"]), 2)
        alto = round(float(cotacao["BTCBRL"]["high"]), 2)

        print(Fore.YELLOW + "Moeda: " + cotacao["BTCBRL"]["name"])
        print(Fore.CYAN + "Valor mais alto do Bitcoin: R$" + str(alto))
        print(Fore.CYAN + "Valor mais baixo do Bitcoin: R$" + str(baixo))
        print("----------------")

    else:
        print(Fore.RED + "Erro ao obter a cotação da moeda:", moeda)
        print("----------------")    
    

    sleep(3)