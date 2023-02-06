import requests
import json
from json.decoder import JSONDecodeError

# payload = {"name": "Igor"}
response = requests.get("https://playground.learnqa.ru/api/get_text", params={"name": "Igor"})

try:
    parsed_response = response.json()
    # print(response.text)
    print(parsed_response)
except JSONDecodeError:
    print("response is not json format")


