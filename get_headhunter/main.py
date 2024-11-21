from src.vacancies import Vacancies
from src.file_json import FilesJSON
from src.list_vacancies import ListVacansies
from src.get_api import GetAPI

def main():


    api = GetAPI('бухгалтер')
    print(api.data)

    print(api.status)

    vacansies_data = ListVacansies.tp_dict(api.data)

    print(vacansies_data)

    #x =   Vacancies()
    #x.created(vacansies_data)

    #f = FilesJSON('112sd.txt')


    #q:list = f.data_json_created(x.vacancies)
    #w = f.save(q)

    #vacansies_data = f.read()
    #print(vacansies_data)
    #x.created(vacansies_data)

    #print(x)
    #for v in x.vacancies:
     #   print(v.__dict__)




if __name__ == "__main__":
    main()