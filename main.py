import requests
from colorama import Fore, init

init(autoreset=True)

def check_github_username(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f"{Fore.GREEN}[Yes] {username}")
    elif response.status_code == 200:
        print(f"{Fore.RED}[No] {username}")
    else:
        print(f"ERROR {username}")

def check_usernames_from_file(filename):
    with open(filename, 'r') as file:
        usernames = file.readlines()
    
    usernames = [username.strip() for username in usernames]
    
    for username in usernames:
        check_github_username(username)

if __name__ == '__main__':
    filename = 'users.txt'  
    check_usernames_from_file(filename)
