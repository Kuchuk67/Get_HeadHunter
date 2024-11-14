import pytest
from unittest.mock import patch
from src.get_api import GetAPI
class Test_(GetAPI):
    def vacancies(self):
        pass


@patch("requests.get")
def test_class_get_api(mock_get):
    x = Test_()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"items":[{"id":"93353083","premium":False,"name":"Тестировщик комфорта квартир"}]}
    x.load_vacancies('Бухгалтер')
    assert  x.vacancies_data == [
        {'id': '93353083', 'premium': False, 'name': 'Тестировщик комфорта квартир'},
        {'id': '93353083', 'premium': False, 'name': 'Тестировщик комфорта квартир'}
    ]

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value ={}
    x.load_vacancies('Бухгалтер')
    assert x.vacancies_data == []
    assert x.status == 404