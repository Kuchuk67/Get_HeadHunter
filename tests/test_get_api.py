import pytest
from unittest.mock import patch
from src.get_api import GetAPI

@pytest.mark.parametrize("get_api", [{"items":[{"id":"93353083","premium":False,"name":"Дворник"},]}
                                     ])


@patch("requests.get")
def test_class_get_api(mock_get, get_api):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = get_api
    test_object = GetAPI('бухгалтер')
    print(test_object.data)
    print(test_object.status)

    #assert test_object.data ==
    assert  test_object.data == [
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'},
        {'id': '93353083', 'premium': False, 'name': 'Дворник'}
    ]
    assert test_object.status == 200
