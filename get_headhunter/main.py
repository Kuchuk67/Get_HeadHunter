from src.vacancies import Vacancies, IterVacancies
from src.file_json import FilesJSON
from src.list_vacancies import ListVacansies
from src.get_api import GetAPI
from src.vacancy import CompareVacancies

def main():


    #api = GetAPI('бухгалтер')
    #print(api.data)

    #print(api.status)
    #api = ListVacansies('бухгалтер')
    #x = api.connect()
    #print(x)

    #vacansies_data = api.to_dict()

    #print(vacansies_data)

    #x =   Vacancies()
    #x.created(vacansies_data)

    f = FilesJSON('112sd.txt')

    #f.remove()
    #q:list = f.data_json_created(x.vacancies)
    #w = f.save(q)

    vacansies_data = f.read()
    #print(vacansies_data)
    x = Vacancies()
    x.created(vacansies_data)

    q: list = f.data_json_created(x.vacancies)
    w = f.save(q)

    print(w)
    #for v in x.vacancies:
     #   print(v.__dict__)


    """f = IterVacancies(x.vacancies)
    for _ in range(10):

        print(next(f))

    compare = CompareVacancies(x.vacancies[0])
    print(compare(x.vacancies[1]))
    print(compare(x.vacancies[2]))
    print(compare(x.vacancies[3]))"""

    #print(CompareVacancies(x.vacancies[0], x.vacancies[1]))






if __name__ == "__main__":
    main()