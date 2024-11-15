import requests
import time
#from pyflakes.checker import counter
from abc import ABC, abstractmethod


class GetAPI(ABC):
    """абстрактный класс для работы с API сервиса с вакансиями.
    создаст объект: список словарей с данными"""

    def __init__(self,file_name:str):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 2, 'area': 113}
        self.status:int = 0
        self.__vacancies_data: list = []
        super().__init__(file_name)


    def load_vacancies(self, keyword):
        self.params['page'] = 0
        self.params['text'] = keyword
        #self.__vacancies = []
        while self.params.get('page') != 2:
            for _ in range(3):
                response = requests.get(self.url, headers=self.headers, params=self.params)
                self.status = response.status_code
                if self.status == 200:
                    break
                time.sleep(3)
            if self.status != 200:
                self.__vacancies_data = []
                break

            vacancies_page = response.json()['items']
            self.__vacancies_data.extend(vacancies_page)

            self.params['page'] += 1

    @abstractmethod
    def vacancies(self):
        """ Метод который будет выводить вакансии в нужном виде и формате"""
        pass

    @property
    def vacancies_data(self):
        """ метод выводит полученные по API вакансии"""
        return self.__vacancies_data

    @vacancies_data.deleter
    def vacancies_data(self):
        self.__vacancies_data = []

