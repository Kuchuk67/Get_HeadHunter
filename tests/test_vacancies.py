import pytest

from src1.vacancies import Vacancies
from src1.vacancy import Vacancy
from unittest.mock import patch

@patch("requests.get")
def test_vacancies(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [{'id': 12345,'name': 'Главный бухгалтер',
'salary': {'from': None, 'to': 450000, 'currency': 'RUR', 'gross': False},
'address':{'city': 'Москва', 'street': 'Московский международный деловой центр Москва-Сити'},
'published_at': '2024-11-14T16:18:47+0300',
'url': 'https://api.hh.ru/vacancies/110985627?host=hh.ru',
'snippet': {'requirement': 'Опыт работы главным <highlighttext>бухгалтером</highlighttext>',} }]}
    test_object = Vacancies('111.json')
    test_object.load_vacancies('Бухгалтер')


    assert test_object.vacancies[0].name == 'Главный бухгалтер'
   # assert test_object.vacancies[1].address == 'Москва, Московский международный деловой центр Москва-Сити'
    assert test_object.vacancies[0].url == 'https://api.hh.ru/vacancies/110985627?host=hh.ru'
    assert test_object.vacancies[1].additionally == {'snippet': 'Опыт работы главным бухгалтером',
                                                     'schedule': '',
                                                     'address': 'Москва, Московский международный деловой центр Москва-Сити'}

    a = len(test_object.vacancies)
    test_object.vacancy_del(12345)
    b = len(test_object.vacancies)
    assert b == a - 1



    del test_object.vacancies
    del test_object.vacancies_data
    assert test_object.vacancies == []

def test_compare_vacancies():
    a = Vacancy(1, 'Дворник', 12000, 15000, 'RU','http://#','2024-02-16T14:58:28+0300',{'snippet': 'Чисто подметать двор', 'schedule': 'Без выходных>', 'address': 'Москва, улица Шаболовка'} )
    b = Vacancy(2, 'Дворник', 30000, 50000, 'RU', 'http://#','2024-02-16T14:58:28+0300', {'snippet': 'Не пить на работе', 'schedule': 'Без выходных>', 'address': 'Смоленск'} )
    assert a.compare_vacancies(b) == False
    assert b.compare_vacancies(a) == True
    with pytest.raises(ValueError):
        c = Vacancy(3, 'Дворник', 30000, 50000, 'RU',
                    '', '2024-02-16T14:58:28+0300',
                    {'snippet': 'Не пить на работе', 'schedule': 'Без выходных>', 'address': 'Смоленск'})
    with pytest.raises(ValueError):
        d = Vacancy(4, '', 30000, 50000, 'RU',
                    'http:/#', '2024-02-16T14:58:28+0300',
                    {'snippet': 'Не пить на работе', 'schedule': 'Без выходных>', 'address': 'Смоленск'})