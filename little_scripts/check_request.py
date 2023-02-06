import requests

payload ={"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# first = response.history[0]
cookies_value = response1.cookies.get("auth_cookie")

print(cookies_value)

cookies = {}
if cookies_value is not None:
    cookies.update({"auth_cookie": cookies_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)
# print(first.url)
# print(dict(response.cookies))


