import re

from src.get_api import GetAPI


class Vacancy:
    '''Класс вакансии. Объект содежит данные по одной вакансии'''
    def __init__(self,name, salary_from, salary_to, currency,  address, url, snippet, schedule):
        self.__name:str = name
        if salary_to:
            self.__salary_to:int = salary_to
        else:
            self.__salary_to = 0
        if salary_from:
            self.__salary_from:int = salary_from
        else:
            self.__salary_from = 0

        self.__address:str = address
        self.__url:str = url
        self.__snippet:str = snippet
        self.__schedule:str = schedule
        self.__currency:str  = currency

    @property
    def name(self):
        return self.__name

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def currency(self):
        return self.__currency

    @property
    def address(self):
        return self.__address

    @property
    def url(self):
        return self.__url

    @property
    def schedule(self):
        return self.__schedule

    @property
    def snippet(self):
        if self.__snippet:
            snippet = re.sub('(<(/?[^>]+)>)', '', self.__snippet)
        else:
            snippet = ''
        return snippet


class Vacancies(GetAPI):
    """ Содержит загруженные по API вакансии"""
    def __init__(self):
        self.__vacancies = []
        super().__init__()

    
    @property
    def vacancies(self):
        '''Отдает список объектов с вакансиями'''
        if self.__vacancies == [] and not self.vacancies_data == []:
            for vacancy in self.vacancies_data:

                if vacancy.get('address'):
                    address = f"{vacancy.get('address').get('city')}, {vacancy.get('address').get('street')}"
                else: address = ""
                dict_salary = vacancy.get('salary')
                if vacancy.get('salary'):
                    salary_to = vacancy.get('salary', "0").get('to', "0")
                    salary_from = vacancy.get('salary', "0").get('from', "0")

                    if  not salary_to:
                        salary_to = 0
                    salary_to = int(salary_to)

                    if not salary_from:
                        salary_from = 0
                    salary_from = int(salary_from)

                    currency = f'{vacancy.get('salary').get('currency', "")}'
                else:
                    salary_to = 0
                    salary_from = 0
                    currency = ''

                if vacancy.get('snippet'):
                    snippet = f"{vacancy.get('snippet').get('requirement')}"
                else:
                    snippet = ""

                if vacancy.get('schedule'):
                    schedule = f"{vacancy.get('schedule').get('name')}"
                else: schedule = ""


                self.__vacancies.append( Vacancy(vacancy.get('name'),
                                                 salary_from,
                                                 salary_to,
                                                 currency,
                                                 address,
                                                 vacancy.get('url'),
                                                 snippet,
                                                 schedule
                                                 ))

        return self.__vacancies

    @vacancies.deleter
    def vacancies(self):
        '''Удаляет все вакансии'''
        self.__vacancies = []
        #del self.vacancies_data





x = Vacancies()
#del x.vacancies
x.load_vacancies('бухгалтер')


print(x.vacancies_data)
print(x.vacancies)
for v in x.vacancies:
    print(v.name, ' - ',v.snippet, v.salary_from, '-' , v.salary_to, v.currency,  v.address, v.schedule, v.url)

del x.vacancies
print(x.vacancies)
