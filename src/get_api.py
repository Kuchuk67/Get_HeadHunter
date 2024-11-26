import requests
import time
from abc import ABC, abstractmethod
from config import PAGE, PER_PAGE, AREA

class GetAPI(ABC):
    """ отправляет запрос для получения данных API
    создаст объект: список словарей с данными """

    def __init__(self, keyword):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': PER_PAGE, 'area': AREA}
        self.status:int = 0
        self.__vacancies_data: list = []


        self.__params['page'] = 0
        self.__params['text'] = keyword

    @property
    def area(self):
        """ параметр area длф API запроса"""
        return self.__params['area']

    @area.setter
    def area(self, data):
        """ изменение параметра area длф API запроса"""
        self.__params['area'] = data

    @property
    def salary(self):
        """ параметр salary длф API запроса"""
        return self.__params['salary']

    @salary.setter
    def salary(self, data):
        """ изменение параметра salary длф API запроса"""
        self.__params['salary'] = data



    @abstractmethod
    def to_dict(self):
        pass


    def connect(self):
        """ делает API запрас,
        сохраняет статус-код запроса.
        если статус 200 возвращает словарь с JSON данными"""
        while self.__params.get('page') != PAGE:

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

