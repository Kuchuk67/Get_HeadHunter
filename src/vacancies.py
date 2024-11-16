
from src.abc_save import Save_Vacancies
from src.list_vacancies import ListVacancies
from src.save_json import SaveJSON


class Vacancies(SaveJSON, ListVacancies):
    """ Содержит Save_Vacanciesзагруженные по API вакансии"""
    def __init__(self,file_name:str):

        super().__init__(file_name)











