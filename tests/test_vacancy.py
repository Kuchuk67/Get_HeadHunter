from src.vacancy import Vacancy, CompareVacancies
import pytest


def test_compare_vacancies():
    a = Vacancy(1, 'Дворник', 12000, -12, 'RU', 'http://#', '2024-02-16T14:58:28+0300',
                {'snippet': 'Чисто подметать двор', 'schedule': 'Полный день',
                 'address': 'Москва, Космодамианская набережная'}
                )
    b = Vacancy(2, 'Дворник', 30000, 50000, 'RU', 'http://#', '2024-02-16T14:58:28+0300',
                {'snippet': 'Не пить на работе', 'schedule': 'Полный день',
                 'address': 'Москва, Космодамианская набережная'} )
    comple = CompareVacancies(a)
    assert comple(b) == False
    comple = CompareVacancies(b)
    assert comple(a) == True


def test_compare_none():
    with pytest.raises(ValueError):
        c = Vacancy(3, 'Дворник', 12000, 15000, 'RU', '', '2024-02-16T14:58:28+0300',
                {'snippet': 'Чисто подметать двор', 'schedule': 'Полный день',
                 'address': 'Москва, Космодамианская набережная'})
    with pytest.raises(ValueError):
        d = Vacancy(4, '', 12000, 15000, 'RU', 'http://#', '2024-02-16T14:58:28+0300',
                {'snippet': 'Чисто подметать двор', 'schedule': 'Полный день',
                 'address': 'Москва, Космодамианская набережная'})


