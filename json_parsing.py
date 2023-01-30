import json
import requests



# string_as_json_format = '{"answer": "Hello, User"}'
# obj = json.loads(string_as_json_format)
# key = "answer"
#
# if key in obj:
#     print(obj[key])
# else:
#     print(f"{key} of json does not were")

# json_text = "https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37"
# obj = json.loads('response')
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

obj = json.loads(json_text)

print(obj["messages"][1]["message"])