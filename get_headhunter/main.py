
from src.get_api import GetAPI
from src.list_vacancies import ListVacansies
from src.vacancies import Vacancies
from src.file_json import FilesJSON

def main():


    api = GetAPI('бухгалтер')

    print(api.status)

    vacansies_data = ListVacansies.tp_dict(api.data)

    x =   Vacancies()
    x.created(vacansies_data)

    f = FilesJSON('112sd.txt')

    q:list = f.data_json(x.vacancies)


    w = f.save(q)

    #w = f.read()

    print(w)











if __name__ == "__main__":
    main()