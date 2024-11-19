from src1.list_vacancies import ListVacancies
from src1.save_json import SaveJSON


class Vacancies(SaveJSON, ListVacancies):
    """ Класс работы с вакансиями загруженными с HeadHunter по API
    Создание списка вакансий. Сортировка по дате и зарплате.
    Итерирование списка. Удаление ненужных вакансий.
    Сохрание и чтение файла со списком в формате JSON"""
    def __init__(self,file_name:str):
       super().__init__(file_name)











