from src.vacancy import Vacancy
from src.abc_get_api import GetAPI

class ListVacancies(GetAPI):
    
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
                else:
                    address = ""
                # dict_salary = vacancy.get('salary')
                if vacancy.get('salary'):
                    salary_to = vacancy.get('salary', "0").get('to', "0")
                    salary_from = vacancy.get('salary', "0").get('from', "0")

                    if not salary_to:
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
                else:
                    schedule = ""

                self.__vacancies.append(Vacancy(vacancy.get('name'),
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
        # del self.vacancies_data