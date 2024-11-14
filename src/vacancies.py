from src.get_api import GetAPI

class Vacancies(GetAPI):


    def vacancies(self):
        print(self.vacancies_data)



x = Vacancies()

x.load_vacancies('Бухгалтер')


print(x.vacancies_data)

