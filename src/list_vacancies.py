import re
from src.vacancy import Vacancy

class ListVacansies:
    """ переводит формат JSON HH.ru
в список словарей с данными по вакансии """

    def __init__(self, vacancies_data:list):
        self.vacancies_data = vacancies_data
    def __str__(self) -> list:
        vacancies:list = []
        for vacancy in vacancies_data:

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

            additionally = {'snippet': snippet, 'schedule': schedule, 'address': address}

            try:
                vacancies.append(Vacancy(vacancy.get('id'),
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

        return vacancies
