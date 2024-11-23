import requests
import time
from abc import ABC, abstractmethod

class GetAPI(ABC):
    """ отправляет запрос для получения данных API
    создаст объект: список словарей с данными"""

    def __init__(self, keyword):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100, 'area': '113'}
        self.status:int = 0
        self.__vacancies_data: list = []



        self.__params['page'] = 0
        self.__params['text'] = keyword

    @property
    def area(self):
        return self.__params['area']

    @area.setter
    def area(self, data):
        self.__params['area'] = data




    @abstractmethod
    def to_dict(self):
        pass


    def connect(self):
        while self.__params.get('page') != 5:

            for _ in range(3):
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                self.status = response.status_code
                if self.status == 200:
                    break
                time.sleep(3)
            if self.status != 200:
                self.__vacancies_data = []
                break

            vacancies_page = response.json()['items']
            self.__vacancies_data.extend(vacancies_page)

            self.__params['page'] += 1

        return self.status


    @property
    def data(self):
        """ метод выводит полученные по API вакансии"""
        return self.__vacancies_data

    @data.deleter
    def data(self):
        self.__vacancies_data = []

