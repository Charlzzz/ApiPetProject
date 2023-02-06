'''Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой.
 И какой URL итоговый.
Ответ опубликуйте в виде ссылки на коммит со скриптом, а также укажите количество редиректов и конечный URL.'''
import requests

resp = requests.get("https://playground.learnqa.ru/api/long_redirect")
resp_history = resp.history
for dir in resp_history:
    print(dir.url)
print(f"Total redirect - {len(resp_history)}, End dir in history is {resp_history[-1].url}")