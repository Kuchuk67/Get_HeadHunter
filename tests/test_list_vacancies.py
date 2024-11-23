from src.list_vacancies import ListVacansies
import pytest

from unittest.mock import patch
from src.get_api import GetAPI

@pytest.mark.parametrize("get_api", [{"items":[{"id":"93353083","premium":False,"name":"Дворник"},]}
                                     ])


@patch("requests.get")
def test_list_vacancies(mock_get, get_api):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = get_api
    test_object = ListVacansies('бухгалтер')
    result = test_object.to_dict()

    assert  test_object.data == [
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'}
    ]
    assert test_object.status == 200

    assert result == [{'_Vacancy__id_v': '93353083', '_Vacancy__name': 'Дворник', '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 0,
      '_Vacancy__currency': '', '_Vacancy__url': None, '_Vacancy__date': None,
      '_Vacancy__additionally': {'snippet': '', 'schedule': '', 'address': ''}},
     {'_Vacancy__id_v': '93353083', '_Vacancy__name': 'Дворник', '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 0,
      '_Vacancy__currency': '', '_Vacancy__url': None, '_Vacancy__date': None,
      '_Vacancy__additionally': {'snippet': '', 'schedule': '', 'address': ''}},
     {'_Vacancy__id_v': '93353083', '_Vacancy__name': 'Дворник', '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 0,
      '_Vacancy__currency': '', '_Vacancy__url': None, '_Vacancy__date': None,
      '_Vacancy__additionally': {'snippet': '', 'schedule': '', 'address': ''}},
     {'_Vacancy__id_v': '93353083', '_Vacancy__name': 'Дворник', '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 0,
      '_Vacancy__currency': '', '_Vacancy__url': None, '_Vacancy__date': None,
      '_Vacancy__additionally': {'snippet': '', 'schedule': '', 'address': ''}},
     {'_Vacancy__id_v': '93353083', '_Vacancy__name': 'Дворник', '_Vacancy__salary_from': 0, '_Vacancy__salary_to': 0,
      '_Vacancy__currency': '', '_Vacancy__url': None, '_Vacancy__date': None,
      '_Vacancy__additionally': {'snippet': '', 'schedule': '', 'address': ''}}]





