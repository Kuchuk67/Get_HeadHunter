from src.vacancies import Vacancies
from src.vacancy import Vacancy
from unittest.mock import patch

@patch("requests.get")
def test_vacancies(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [{'name': 'Главный бухгалтер',
'salary': {'from': None, 'to': 450000, 'currency': 'RUR', 'gross': False},
'address':{'city': 'Москва', 'street': 'Московский международный деловой центр Москва-Сити'},
'published_at': '2024-11-14T16:18:47+0300',
'url': 'https://api.hh.ru/vacancies/110985627?host=hh.ru',
'snippet': {'requirement': 'Опыт работы главным <highlighttext>бухгалтером</highlighttext>',} }]}
    test_object = Vacancies('111.json')
    test_object.load_vacancies('Бухгалтер')




    assert test_object.vacancies[0].name == 'Главный бухгалтер'
    assert test_object.vacancies[1].address == 'Москва, Московский международный деловой центр Москва-Сити'
    assert test_object.vacancies[0].url == 'https://api.hh.ru/vacancies/110985627?host=hh.ru'
    assert test_object.vacancies[1].snippet == 'Опыт работы главным бухгалтером'

    del test_object.vacancies
    del test_object.vacancies_data
    assert test_object.vacancies == []

def test_compare_vacancies():
    a = Vacancy('Дворник', 12000, 15000, 'RU','Смоленск', '', 'Чисто подметать двор', '')
    b = Vacancy('Дворник', 30000, 50000, 'RU', 'Смоленск', '', 'Не пить на работе', '')
    assert a.compare_vacancies(b) == False
    assert b.compare_vacancies(a) == True