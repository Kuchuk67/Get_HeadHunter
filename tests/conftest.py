from src.abc_get_api import GetAPI
from src.abc_save import Save_Vacancies
import pytest

class Test_GetAPI(GetAPI, Save_Vacancies):
    def vacancies(self):
        pass
    def add(self):
        pass

    def read(self):
        pass

    def remove(self):
        pass

@pytest.fixture
def test_object():
    return Test_GetAPI('111.json')