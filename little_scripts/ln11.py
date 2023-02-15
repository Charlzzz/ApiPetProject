#Ex11: Тест запроса на метод cookie
#Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
#Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert
#Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py


import requests
import pytest

class TestApi():

    def test_check_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        assert response.status_code == 200, "Bad request, status code is not 200"

        cookies = dict(response.cookies)
        print(cookies)
        assert cookies['HomeWork'] == 'hw_value', 'Cookies is`not valid'
