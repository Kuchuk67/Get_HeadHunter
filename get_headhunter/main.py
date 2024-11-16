from src.vacancies import Vacancies
from src.abc_get_api import GetAPI
from src.save_json import SaveJSON

def main():


    x = Vacancies('111.json')
    #x.load_vacancies('бухгалтер')

    #print(x.vacancies_data)
    #print(x.vacancies)
    for v in x.vacancies:
        print(v.id_v, v.name, ' - ', v.snippet, v.salary_from, '-', v.salary_to, v.currency, v.address, v.schedule, v.url)

    #del x.vacancies
    #print(x.vacancies)

    #x.remove()

    #x.save()

    x.read()
    #print(x.vacancies)

    #x.vacancy_del('https://api.hh.ru/vacancies/111052269?host=hh.ru')
    x.sort_date()
    for v in x.vacancies:
        print(v.id_v,  v.salary_average, v.name, ' - ', v.snippet, v.currency, v.address, v.schedule, v.url, v.date)

    #print(x.vacancies)

    #sorted_list = sorted(n_list, key=lambda x: int(x[0:]))
    #q = sorted(x.vacancies, key = lambda y: y.id_v )




if __name__ == "__main__":
    main()