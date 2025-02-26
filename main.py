import requests
from colorama import Fore, init

# Инициализация colorama для Windows (если необходимо)
init(autoreset=True)

def check_github_username(username):
    # Отправляем запрос к API GitHub
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    
    if response.status_code == 404:
        # Зеленая галочка для доступного юзернейма
        print(f"{Fore.GREEN}[Yes] {username}")
    elif response.status_code == 200:
        # Красная галочка для занятых юзернеймов
        print(f"{Fore.RED}[No] {username}")
    else:
        print(f"ERROR {username}")

def check_usernames_from_file(filename):
    # Открываем файл и читаем юзернеймы
    with open(filename, 'r') as file:
        usernames = file.readlines()
    
    # Убираем лишние пробелы и новые строки из каждого имени
    usernames = [username.strip() for username in usernames]
    
    # Проверяем каждый юзернейм
    for username in usernames:
        check_github_username(username)

if __name__ == '__main__':
    filename = 'users.txt'  # Файл с юзернеймами
    check_usernames_from_file(filename)
