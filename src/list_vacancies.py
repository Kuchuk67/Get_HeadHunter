import re
from src.vacancy import Vacancy
from src.get_api import GetAPI

class ListVacansies(GetAPI):
    """ переводит формат JSON HH.ru
в список словарей с данными по вакансии """
    def __init__(self, keyword):
        self.__vacancies_data = []
        super().__init__(keyword)



    def to_dict(self):
        vacancies_data = []
        for vacancy in self.data:

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

            dict_ = {'_Vacancy__id_v': vacancy.get('id'), '_Vacancy__name': vacancy.get(
                'name'), '_Vacancy__salary_from': salary_from, '_Vacancy__salary_to': salary_to, '_Vacancy__currency': currency, '_Vacancy__url': vacancy.get(
                'url'), '_Vacancy__date': vacancy.get('published_at'), '_Vacancy__additionally': additionally}
            vacancies_data.append(dict_)
            #print(dict_)


        return vacancies_data
