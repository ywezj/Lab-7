from requests import get
from json import loads


def get_weather_data(city):
    """Получает данные о погоде для указанного города"""
    api_key = '3ddf6ac5a114b2df2ef796cac6796878'
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'
    response = get(url)
    return loads(response.text)


def print_weather_info(json_data):
    """Выводит информацию о погоде"""
    weather = json_data['weather'][0]
    main = json_data['main']
    
    print(
        f"Weather: {weather['main']}, {weather['description']}\n"
        f"Humidity: {main['humidity']}%\n"
        f"Pressure: {main['pressure']}"
    )


if __name__ == '__main__':
    city_name = input('Enter a city name: ')
    weather_data = get_weather_data(city_name)
    print_weather_info(weather_data)