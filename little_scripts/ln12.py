#Ex12: Тест запроса на метод header
#
#Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
#Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert
#
#Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py

import requests, pytest

class TestApi():

    def test_check_header(self):
        url = 'https://playground.learnqa.ru/api/homework_header'
        response = requests.get(url)
        assert response.status_code == 200, "Bad request, status code is not 200"

        headers = dict(response.headers)
        print(headers)
        assert 'Some secret value' == headers['x-secret-homework-header'], 'Headers value  is`not correct'