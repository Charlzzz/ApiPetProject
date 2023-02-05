import requests
import pytest

class TestFirstApi:
    names = [
        ("Vitalii"),
        ("Arsenii"),
        ("")
    ]
    @pytest.mark.parametrize("name", names)
    def test_hello_api(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        # name = 'Vitalii'
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert  expected_response_text == actual_response_text, "Actual text in the response is not correct"