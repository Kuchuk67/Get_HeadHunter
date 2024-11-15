from src.get_api import GetAPI
import pytest

class Test_GetAPI(GetAPI):
    def vacancies(self):
        pass

@pytest.fixture
def test_object():
    return Test_GetAPI()