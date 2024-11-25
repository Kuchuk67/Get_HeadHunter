from src.list_vacancies import ListVacansies
from src.file_json import FilesJSON
from src.area import Area

def load(data, f):

    while True:
        print("\n--- ЗАГРУЗКА  СПИСКА ---")
        print("1. Загрузить вакансии с HH.RU\n2. Загрузить вакансии из файла")
        print("3. Добавить вакансии в файл")
        print("6. Удалить файл\n8. Удалить список вакансий")
        print("0. Выход в меню\n")

        user_input = input("Выберите пункт меню: ")
        if user_input == '0':
            break
        elif user_input == '1': # Загрузить вакансии с HH.RU

            word = input("\nВведите вакансию: ")

            ar = input("\nВведите территорию поиска: ")
            x = Area()
            x.load()
            x.save_to_file()
            q = Area.id_area(ar)
            if q[0] == 'Ok':
                area_id = q[1]
                print(f"Найдены регионы: {q[2]}")
            else:
                print(q[0])
                area_id =  '113'
                print(f"Ошибка. Регион по умолчанию: Россия")
                #q[2] = 'Россия'




            api = ListVacansies(word)
            api.area = area_id
            status = api.connect()
            if status != 200:
                print(f"Ошибка загрузки API: {status}")
            else:
                print("Данные API загружены")
                vacansies_data = api.to_dict()
                data.created(vacansies_data)
        elif user_input == '2':  #  Загрузить вакансии из файла

            data_from_file = f.read()
            data.created(data_from_file)
        elif user_input == '3':  #  Добавить вакансии в файл

            list_data_to_file: list = f.data_json_created(data.vacancies)
            status = f.save(list_data_to_file)
            print(status)
        elif user_input == '6':  #  Удалить файл

            f.remove()
        elif user_input == '8':  #  Удалить список вакансий
            del data.vacancies
        elif user_input == '0': # Выход
            return None


