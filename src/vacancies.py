import re

from src.get_api import GetAPI


class Vacancy():
    '''Класс вакансии. Объект содежит данные по одной вакансии'''
    def __init__(self,name, salary, address, url, snippet):
        self.__name = name
        self.__salary = salary
        self.__address = address
        self.__url = url
        self.__snippet = snippet

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def address(self):
        return self.__address

    @property
    def url(self):
        return self.__url

    @property
    def snippet(self):
        if self.__snippet:
            snippet = re.sub('(<(/?[^>]+)>)', '', self.__snippet)
        else:
            snippet = ''
        return snippet


class Vacancies(GetAPI):
    """ Содержит загруженные по API вакансии"""
    def __init__(self, keyword):
        self.__vacancies = []
        super().__init__()
        # print(self.vacancies_data)
        super().load_vacancies(keyword)

    def load_vacancies(self, keyword):
        pass
    
    @property
    def vacancies(self):
        '''Отдает список объектов с вакансиями'''
        if self.__vacancies == [] and not self.vacancies_data == []:
            for vacancy in self.vacancies_data:
                if vacancy.get('address'):
                    address = f"{vacancy.get('address').get('city')}, {vacancy.get('address').get('street')}"
                else: address = ""
                self.__vacancies.append( Vacancy(vacancy.get('name'),
                                                 vacancy.get('salary').get('to'),
                                                 address,
                                                 vacancy.get('url'),
                                                 vacancy.get('snippet').get('requirement')))
        return self.__vacancies

    @vacancies.deleter
    def vacancies(self):
        '''Удаляет все вакансии'''
        self.__vacancies = []
        del self.vacancies_data






x = Vacancies('Бухгалтер')

x.load_vacancies('Бухгалтер')


print(x.vacancies_data)
print(x.vacancies)
for v in x.vacancies:
    print(v.name, v.snippet)

del x.vacancies
print(x.vacancies)
