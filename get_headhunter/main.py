from src.vacancies import Vacancies
from src.file_json import FilesJSON
from function import len_vac, menu, move
from load import load
from config import FILE_NAME

def main():


    print("\nПрограмма работы со списком вакансий")
    data = Vacancies()
    f = FilesJSON(FILE_NAME)

    while True:
        len_vac(data)
        user_input = menu(data)

        if user_input == '1': # Загрузить вакансии
            load(data, f)
        elif user_input == '2' and len(data.vacancies) > 0: # Сортировать список по дата
            data.sort_date()
        elif user_input == '3' and len(data.vacancies) > 0: # Сортировать список по зарплате
            data.sort_salary()
        elif user_input == '4' and len(data.vacancies) > 0: #  Просмотр списка вакансий
            move(data)
        elif user_input == '6':  # Изменить имя файла
            print(f"\nТекущее имя файла: {f.file_name}.тип")
            file_ = input("Для работы введите имя файла (расширение подставляется автоматически): ")
            if file_.isalnum():
                f = FilesJSON(file_)
            else:
                print("Недопустимый тип файла")
        elif user_input == '8' and len(data.vacancies) > 0: # Удалить список вакансий
            del data.vacancies
        elif user_input == '0': # Выход
            break

if __name__ == "__main__":
    main()