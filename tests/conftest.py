import pytest

from src1.list_vacancies import ListVacancies
from src1.save_json import SaveJSON


class TestGetAPI(SaveJSON, ListVacancies):
    pass

@pytest.fixture
def test_object():
    return TestGetAPI('111.json')