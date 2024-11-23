import pytest

from src.vacancies import Vacancies, IterVacancies
from src.vacancy import Vacancy
from unittest.mock import patch


def test_vacancies(vacansies_data):
    x = Vacancies()
    x.created(vacansies_data)
    assert  x.vacancies[0].name == "Бухгалтер по расчету заработной платы"
    assert  x.vacancies[2].name ==  "Бухгалтер по расчетам"
    assert x.vacancies[0].salary_from == 170000
    assert x.vacancies[1].salary_from == 60000
    assert x.vacancies[0].salary_to == 190000
    assert x.vacancies[3].salary_to == 70000
    assert x.vacancies[0].salary_average == 180000
    assert x.vacancies[1].salary_average == 60000
    assert x.vacancies[0].url == "https://api.hh.ru/vacancies/111529103?host=hh.ru"
    assert x.vacancies[1].date == "2024-11-21T11:11:06+0300"
    assert x.vacancies[2].additionally == {
        'snippet': 'Опыт работы в программе 1С ЗУП 8.3, 1С Бухгалтерия 8.3. Знание нормативных документов. Уверенное владение ПК...',
        'schedule': 'Полный день', 'address': 'Волгоград, Советская улица'}

def test_sort_date(vacansies_data):
    x = Vacancies()
    x.created(vacansies_data)
    x.sort_date()

    assert x.vacancies[0].date == "2024-11-21T16:09:19+0300"
    assert x.vacancies[2].date == "2024-11-20T14:48:19+0300"
    assert x.vacancies[4].date == "2024-08-20T08:39:12+0300"

def test_sort_salary(vacansies_data):
    x = Vacancies()
    x.created(vacansies_data)
    x.sort_salary()

    assert x.vacancies[0].salary_average == 180000
    assert x.vacancies[2].salary_average == 75000
    assert x.vacancies[4].salary_average == 60000


def test_vacancy_del(vacansies_data):
    x = Vacancies()
    x.created(vacansies_data)
    x.vacancy_del(111529103)
    assert x.vacancies[0].id_v != 111529103

def test_del_v(vacansies_data):
    x = Vacancies()
    x.created(vacansies_data)
    del x.vacancies
    assert x.vacancies == []

def test_iter_vacancies(vacansies_data):
    x = Vacancies()
    x.created(vacansies_data)
    f = IterVacancies(x.vacancies)
    q = next(f)
    assert q.name == "Бухгалтер по расчету заработной платы"
    for _ in range(9):
        q = next(f)

    with pytest.raises(StopIteration):
        q = next(f)






