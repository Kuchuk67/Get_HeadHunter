class Vacancy:
    '''Класс вакансии. Объект содежит данные по одной вакансии'''
    __slots__ = ('__id_v',  '__name', '__salary_from', '__salary_to', '__salary_average', '__currency',  '__url', '__date', '__additionally')

    def __init__(self, id_v,  name, salary_from, salary_to, currency,  url, date, additionally):

        self.__id_v:int = id_v
        self.__name:str = name
        self.__salary_from: int = self.valid(salary_from)
        self.__salary_to: int = self.valid(salary_to)

        self.__salary_average: int = CompareVacancies.average(self.__salary_from, self.__salary_to)
        self.__url: str = url
        self.__currency: str = currency
        self.__date: str = date
        self.__additionally: dict = additionally



        if not name  or not url:
            raise ValueError("Ошибка создания вакансии")

    @staticmethod
    def valid(data) -> int:
        if data:
            result:int = data
        else:
            result = 0
        if data < 0:
            result = 0
        return result


    @property
    def id_v(self) -> int:
        return self.__id_v

    @property
    def name(self) -> str:
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
    def url(self):
        return self.__url

    @property
    def additionally(self):
        return self.__additionally

    @property
    def date(self):
        return self.__date






    """def compare_vacancies(self, other):
        salary_1 = Vacancy.average(self.__salary_from, self.__salary_to)
        salary_2 = Vacancy.average(other.__salary_from, other.__salary_to)
        if salary_1 > salary_2:
            return True
        return False"""

class CompareVacancies:
    """Класс, удаляющий определенные символы из строки"""
    def __init__(self, a):
        """Инициализация символов для удаления"""
        self.a = a


    @staticmethod
    def average(from_, to_):
        if from_ == 0:
            from_ = to_
        if to_ == 0:
            to_ = from_
        return (from_ + to_) // 2

    def __call__(self, b):

        salary_1 = CompareVacancies.average(self.a.salary_from, self.a.salary_to)
        salary_2 = CompareVacancies.average(b.salary_from, b.salary_to)
        if salary_1 > salary_2:
            return True
        return False

