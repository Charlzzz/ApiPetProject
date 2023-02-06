#Ex8: Токены

#Иногда API-метод выполняет такую долгую задачу, что за один HTTP-запрос от него нельзя сразу получить готовый ответ.
#Это может быть подсчет каких-то сложных вычислений или необходимость собрать информацию по разным источникам.
#В этом случае на первый запрос API начинает выполнения задачи, а на последующие ЛИБО говорит, что задача еще не готова,
#ЛИБО выдает результат. Сегодня я предлагаю протестировать такой метод.
#Сам API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job

#Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:

#* seconds - количество секунд, через сколько задача будет выполнена
#* token - тот самый токен, по которому можно получить результат выполнения нашей задачи

#Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:

#* error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе будет следующая надпись - No job linked to this token
#* status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
#* result - будет только в случае, если задача готова, это поле будет содержать результат

#Наша задача - написать скрипт, который делал бы следующее:

#1) создавал задачу
#2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
#3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
#4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

import time
import json
import requests

url = "https://playground.learnqa.ru/ajax/api/longtime_job"


def req_before(new_task):
    parsed_response = new_task.json()
    params = {"token": parsed_response["token"]}
    task_before = requests.get(url, params=params)
    parsed_time = parsed_response["seconds"]
    parsed_task_before = task_before.json()
    if parsed_task_before["status"] == "Job is NOT ready":
        time.sleep(parsed_time)
        wight_time(params)


def wight_time(params):
    params_after = params
    task_after = requests.get(url, params=params_after)
    parsed_task_after = task_after.json()
    if parsed_task_after["status"] == "Job is ready":
        print(parsed_task_after["result"])
        print("Well done!!")
    else:
        print("error")


if __name__ == "__main__":
    start_task = requests.get(url)
    req_before(start_task)
