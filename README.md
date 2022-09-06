# Парсер погоды

## Описание:
1. Зарегестировался на сайте: https://home.openweathermap.org/api_keys
2. Получил персональный ключ для доступа к API
3. Записал ключ в apikey.py
4. Импортировал ключ в данный файл
5. На странице https://openweathermap.org/current находим "Built-in API request by city name"
6. API call - https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
7. Нам понадобится https://api.openweathermap.org/data/2.5/weather
8. Остальное передаем параметрами через params
