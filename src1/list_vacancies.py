from src1.vacancy import Vacancy
from src1.abc_get_api import GetAPI
import re

class ListVacancies(GetAPI):
    """Формирует из данных полученных по API  список с объектами вакансий,
добавляет объекты, сортирует список, удаляет объекты из списка"""
    
    def __init__(self):
        self.__vacancies = []
        super().__init__()

    @property
    def vacancies(self) -> list:
        """Отдает список объектов с вакансиями"""
        if self.__vacancies == [] and not self.vacancies_data == []:
            for vacancy in self.vacancies_data:


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
                    snippet = re.sub('(<(/?[^>]+)>)', '', snippet)
                else:
                    snippet = ""

                if vacancy.get('schedule'):
                    schedule = f"{vacancy.get('schedule').get('name')}"
                else:
                    schedule = ""

                if vacancy.get('address'):
                    address = f"{vacancy.get('address').get('city')}, {vacancy.get('address').get('street')}"
                else:
                    address = ""

                additionally = {'snippet':snippet,'schedule':schedule,'address':address}


                try:
                    self.__vacancies.append(Vacancy(vacancy.get('id'),
                                                vacancy.get('name'),
                                                salary_from,
                                                salary_to,
                                                currency,
                                                vacancy.get('url'),
                                                vacancy.get('published_at'),
                                                additionally
                                                ))
                except ValueError as txt:
                    print(f"Вакансия не добавлена: {txt}")

        return self.__vacancies

    @vacancies.setter
    def vacancies(self, data):
        self.__vacancies.append(data)

    @vacancies.deleter
    def vacancies(self):
        """Удаляет все вакансии"""
        self.__vacancies = []
        # del self.vacancies_data


    def vacancy_del(self, id_v) -> None:
        """Удаляет  вакансию"""
        for index, object_vacancy in enumerate(self.vacancies):
            #print(index," - ",object_vacancy.id_v)
            if object_vacancy.id_v == id_v:
                del self.vacancies[index]
                break


    def sort_date(self) -> None:
        """ Сортирует список вакансий по дате """
        sort_vacancies = sorted(self.vacancies, key=lambda x: x.date, reverse=True)
        self.__vacancies = sort_vacancies


    def sort_salary(self) -> None:
        """ Сортирует список вакансий по зарплате """
        sort_vacancies = sorted(self.vacancies,  key=lambda x: x.salary_average, reverse=False)
        self.__vacancies = sort_vacancies


