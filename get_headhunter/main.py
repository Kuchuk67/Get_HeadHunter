from src.vacancies import Vacancies, IterVacancies
from src.file_json import FilesJSON
from src.list_vacancies import ListVacansies
from src.area import Area
from src.get_api import GetAPI
from src.vacancy import CompareVacancies

def main():
    def len_vac():
        #if data.vacansies:
        print(f"В списке загружено вакансий: {len(data.vacancies)}")

    def menu():
        print("\n--- МЕНЮ --- \n1. Загрузить вакансии")
        if len(data.vacancies) > 0:
            print("2. Сортировать список по дата\n3. Сортировать список по зарплате")
            print("4. Просмотр списка вакансий\n8. Удалить список вакансий")
            print("8. Удалить список вакансий")
        print("0. Выход")
        user_input = input("Выберите пункт меню: ")
        return user_input

    print("Программа работы со списком вакансий")
    data = Vacancies()
    len_vac()
    user_input = menu()




    api = ListVacansies('бухгалтер')


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

    #f = FilesJSON('112sd.txt')

    #f.remove()
    #q:list = f.data_json_created(x.vacancies)
    #w = f.save(q)

    #vacansies_data = f.read()
    #print(vacansies_data)
    #x = Vacancies()
    #x.created(vacansies_data)

    #q: list = f.data_json_created(x.vacancies)
    #w = f.save(q)

    #print(w)
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



    #x = Area()
    #x.load()
    #x.save_to_file()
    #q = Area.id_area('')
    #if q[0] == 'Ok':
    #    qq = q[1]
    #    #print(q)
    #else:
     #   print(q[0])
      #  qq =  '113'
        #q[2] = 'Россия'



    #api = ListVacansies('бухгалтер')
    #api.area = qq
    #x = api.connect()
    #print(x)

    #vacansies_data = api.to_dict()

    #print(vacansies_data)



if __name__ == "__main__":
    main()