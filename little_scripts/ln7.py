# Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE

# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос.
# Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом -
# то параметр method должен равняться ‘POST’. И так далее.
#
# Надо написать скрипт, который делает следующее:
#
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
#
# Не забывайте, что для GET-запроса данные надо передавать через params=
# А для всех остальных через data=
import requests
from requests import get, post, put, delete


url = "https://playground.learnqa.ru/ajax/api/compare_query_type"



'''1ex'''
print("1ex")
resp = requests.get(url)
print(resp.text)




'''2ex'''
print("2ex")
params1 = {"method": "HEAD"}
resp1 = requests.get(url, params=params1)
print(resp1.text)



'''3ex'''
print("3ex")
params2 = {"method": "GET"}
resp2 = requests.get(url, params=params2)
print(resp2.text)



'''4ex'''
print("4ex")
def get_req(method_req):
    methods = ['POST', "GET", "PUT", "DELETE"]
    for key in methods:
            params = {'method': key}
            res_req = method_req(url, params=params) if method_req == get else method_req(url, data=params)
            print(f"Метод запроса - {res_req.request.method}\n"
                  f"Payload -{params}\nРезультат - {res_req.text}\n{res_req.url}\n\n")



if __name__ == '__main__':
    for x in [get, post, put, delete]:
        get_req(x)