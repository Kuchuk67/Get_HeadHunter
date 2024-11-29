import pytest
from src.area import Area
from unittest.mock import patch

@pytest.fixture()
def x():
    return [{"id": "113", "parent_id": None, "name": "Россия", "areas": [{"id": "1620", "parent_id": "113", "name": "Республика Марий Эл","areas": [{"id": "4228", "parent_id": "1620", "name": "Виловатово", "areas": []},{"id": "1621", "parent_id": "1620", "name": "Волжск", "areas": []},{"id": "1622", "parent_id": "1620", "name": "Звенигово", "areas": []},{"id": "4229", "parent_id": "1620", "name": "Знаменский", "areas": []},{"id": "61", "parent_id": "1620", "name": "Йошкар-Ола", "areas": []},{"id": "4230", "parent_id": "1620", "name": "Кельмаксола", "areas": []},{"id": "4231", "parent_id": "1620", "name": "Килемары", "areas": []} ]    }    ]  }    ]

@patch("requests.get")
def test_area(mock_get, x):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = x

    data = Area()
    data.load()
    data.save_to_file()
    q = Area.id_area('ЗнаМенский')
    assert q == ('Ok', ['4229'], 'Знаменский')


