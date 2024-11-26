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
        """ Проверка на положительные целые числа"""
        if data:
            result:int = data
        else:
            result = 0
        if data < 0:
            result = 0
        return result


    @property
    def id_v(self) -> int:
        """ возвращает id вакансии"""
        return self.__id_v

    @property
    def name(self) -> str:
        """ возвращает имя вакансии"""
        return self.__name

    @property
    def salary_from(self):
        """ возвращает зарплату 'от' вакансии"""
        return self.__salary_from

    @property
    def salary_to(self):
        """ возвращает зарплату 'до' вакансии"""
        return self.__salary_to

    @property
    def salary_average(self):
        """ возвращает среднюю зарплату вакансии"""
        return self.__salary_average

    @property
    def currency(self):
        """ возвращает валюту зарплаты  вакансии"""
        return self.__currency



    @property
    def url(self):
        """ возвращает урл вакансии"""
        return self.__url

    @property
    def additionally(self):
        """ возвращает словарь пользовательских данных вакансии"""
        return self.__additionally

    @property
    def date(self):
        """ возвращает дату вакансии"""
        return self.__date





class CompareVacancies:
    """Класс создает функцию сравнения вакансий по зарплате
    на вход принимает зкземпляр вакансии
    Возвращает TRUE если проверяемая вакансия больше по зарплате"""
    def __init__(self, a):
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

