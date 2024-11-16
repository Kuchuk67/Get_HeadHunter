from src.vacancies import Vacancies
from src.abc_get_api import GetAPI
from src.save_json import SaveJSON

def main():


    x = Vacancies('111.json')
    x.load_vacancies('бухгалтер')

    #print(x.vacancies_data)
    #print(x.vacancies)
    #for v in x.vacancies:
     #   print(v.name, ' - ', v.snippet, v.salary_from, '-', v.salary_to, v.currency, v.address, v.schedule, v.url)

    #del x.vacancies
    #print(x.vacancies)

    #a = SaveJSON.data_json(x.vacancies)
    x.save()

    #x.read()
    #print(x.vacancies)

    for v in x.vacancies:
        print(v.name, ' - ', v.snippet, v.salary_from, '-', v.salary_to, v.currency, v.address, v.schedule, v.url)

    #x.remove()

if __name__ == "__main__":
    main()