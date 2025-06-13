from requests import get
from json import loads


def get_character_data(character_id):
    """Получаем данные о персонаже по ID"""
    url = f'https://rickandmortyapi.com/api/character/{character_id}'
    response = get(url)
    return loads(response.text)


def format_episodes(episodes):
    """Форматируем список эпизодов для вывода"""
    episodes_count = len(episodes)
    prefix = 'Episodes: ' if episodes_count > 1 else 'Episode: '
    episode_numbers = ', '.join(episode[40:] for episode in episodes)
    return prefix + episode_numbers


def print_character_info(character_data):
    """Выводим информацию о персонаже"""
    # Основные поля
    main_fields = ['name', 'status', 'species', 'gender']
    for field in main_fields:
        print(f"{field.capitalize()}: {character_data[field]}")
    
    # Локация
    print(f"Location: {character_data['location']['name']}")
    
    # Эпизоды
    print(format_episodes(character_data['episode']))


if __name__ == '__main__':
    character_id = input('Enter a character ID: ')
    data = get_character_data(character_id)
    print_character_info(data)