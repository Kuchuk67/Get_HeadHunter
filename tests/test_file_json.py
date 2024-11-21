from src.file_json import FilesJSON
from src.vacancies import Vacancies
from src.vacancy import Vacancy
from config import PATH_HOME
import os

def test_file_json(vacansies_data_0, vacansies_data_1, files):


    x = Vacancies()
    x.created(vacansies_data_0)

    f = FilesJSON('test.txt')
    f.remove()

    q: list = f.data_json_created(x.vacancies)
    w = f.save(q)
    assert w =="Ok"


    del x.vacancies
    x.created(vacansies_data_1)
    q: list = f.data_json_created(x.vacancies)
    w = f.save(q)

    assert w == "Ok"

    result = f.read()

    assert  result == files

    f.remove()

    assert os.path.exists(os.path.join(PATH_HOME, "data", 'test.txt')) == False


