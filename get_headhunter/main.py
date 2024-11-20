
from src.get_api import GetAPI
from src.list_vacancies import ListVacansies

def main():


    api = GetAPI('бухгалтер')
    #x.load_vacancies('бухгалтер')
    #print(x)
    print(api.status)

    vacansies_data = ListVacansies.tp_dict(api.data)

    print(vacansies_data)






if __name__ == "__main__":
    main()