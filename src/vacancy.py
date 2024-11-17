import re


class Vacancy:
    '''Класс вакансии. Объект содежит данные по одной вакансии'''
    def __init__(self, id_v,  name, salary_from, salary_to, currency,  address, url, snippet, schedule, date):
        self.__id_v:int = id_v
        self.__name:str = name
        if salary_from:
            self.__salary_from:int = salary_from
        else:
            self.__salary_from = 0
        if salary_to:
            self.__salary_to:int = salary_to
        else:
            self.__salary_to = 0

        self.__salary_average: int = Vacancy.average(self.__salary_from, self.__salary_to)
        self.__address:str = address
        self.__url:str = url
        self.__snippet:str = snippet
        self.__schedule:str = schedule
        self.__currency:str  = currency
        self.__date: str = date

        if not name  or not url:
            raise ValueError("Ошибка создания вакансии")

    @property
    def id_v(self):
        return self.__id_v

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
    def salary_average(self):
        return self.__salary_average

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
    def date(self):
        return self.__date

    @property
    def snippet(self):
        if self.__snippet:
            snippet = re.sub('(<(/?[^>]+)>)', '', self.__snippet)
        else:
            snippet = ''
        return snippet

    @staticmethod
    def average(from_, to_):
        if from_ == 0:
            from_ = to_
        if to_ == 0:
            to_ = from_
        return (from_ + to_) // 2


    def compare_vacancies(self, other):
        salary_1 = Vacancy.average(self.__salary_from, self.__salary_to)
        salary_2 = Vacancy.average(other.__salary_from, other.__salary_to)
        if salary_1 > salary_2:
            return True
        return False

