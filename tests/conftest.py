from src.abc_get_api import GetAPI
from src.abc_save import Save_Vacancies
import pytest

from src.list_vacancies import ListVacancies
from src.save_json import SaveJSON


class TestGetAPI(SaveJSON, ListVacancies):
    pass

@pytest.fixture
def test_object():
    return TestGetAPI('111.json')