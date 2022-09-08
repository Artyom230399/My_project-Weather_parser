import requests
from apikey import API_TOKEN
from colorama import Fore, Back, Style

# Задаем переменную на ввод названия города
City = input("Введите город:")

# Задаем параметры для корректной работы API
params = {"q": City, "appid": API_TOKEN}

# Передаем параметры
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

# Проверяем, что статутс код - ok
if response.ok:
    # response.json() - читаем список, как json, через [] обращаемся к его параметрам
    print(Fore.CYAN + "\tТемпература в горде", City + ":", int(response.json()['main']['temp'] - 273), "°C", '\n',
          "\tОщущается, как:",
          int(response.json()['main']['feels_like'] - 273), "°C")
else:
    print(Fore.RED + "Ошибка!")
