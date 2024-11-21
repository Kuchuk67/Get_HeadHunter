
from src.get_api import GetAPI
from src.list_vacancies import ListVacansies
from src.vacancies import Vacancies

def main():


    api = GetAPI('бухгалтер')
    #x.load_vacancies('бухгалтер')
    #print(x)
    print(api.status)

    vacansies_data = ListVacansies.tp_dict(api.data)

    x =   Vacancies()
    x.created(vacansies_data)

    print(x.vacancies)

    x.vacancy_del(111422410)

    print(x.vacancies)

    del x.vacancies

    print("-",x.vacancies)









if __name__ == "__main__":
    main()