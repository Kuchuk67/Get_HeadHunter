import pytest
from unittest.mock import patch



@patch("requests.get")
def test_class_get_api(mock_get, test_object):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"items":[{"id":"93353083","premium":False,"name":"Тестировщик комфорта квартир"}]}
    test_object.load_vacancies('Бухгалтер')
    assert  test_object.vacancies_data == [
        {'id': '93353083', 'premium': False, 'name': 'Тестировщик комфорта квартир'},
        {'id': '93353083', 'premium': False, 'name': 'Тестировщик комфорта квартир'},
        {'id': '93353083', 'premium': False, 'name': 'Тестировщик комфорта квартир'},
        {'id': '93353083', 'premium': False, 'name': 'Тестировщик комфорта квартир'},
        {'id': '93353083', 'premium': False, 'name': 'Тестировщик комфорта квартир'}
    ]

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value ={}
    test_object.load_vacancies('Бухгалтер')
    assert test_object.vacancies_data == []
    assert test_object.status == 404