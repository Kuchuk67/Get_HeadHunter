from src.vacancies import IterVacancies
from src.vacancy import CompareVacancies


def len_vac(data):
    print(f"\n\nВ списке загружено вакансий: {len(data.vacancies)}")


def menu(data) -> str:
    print("\n--- МЕНЮ --- ")
    print("\033[34m{}".format("1. Загрузить/сохранить вакансии"))
    if len(data.vacancies) > 0:
        print("2. Сортировать список по дата\n3. Сортировать список по зарплате")
        print("4. Просмотр списка вакансий\n8. Удалить список вакансий")
    print("6. Изменить имя файла\n")
    print("0. Выход\n")
    print("\033[0m{}".format("Выберите пункт меню: "), sep="")
    user_input = input()
    return user_input


def move(data) -> None:
    vac:tuple = ()
    list_for_delete = []
    iter_vacancy = IterVacancies(data.vacancies)
    print("\n--- ПРОСМОТР ---\n")
    repeat_ = 0
    compare = None
    while True:
        if repeat_ == 0:
            vac = next(iter_vacancy)
            if compare:
                if compare(data.vacancies[vac[2]]):
                    continue

        print("\033[33m\033[40m\033[1m{}".format(vac[1]))
        repeat_ = 0
        print("\033[0m\033[34m{}".format(
            f"1. Следующая 2. Завершить 3. Подробнее 4. Показывать с зарплатой выше данной 9. Удалить вакансию"))
        print("\033[0m{}".format(" "))
        user_data = input()

        if user_data == '2':  # Завершить
            print(list_for_delete)
            for id_v in list_for_delete:
                print(id_v)
                data.vacancy_del(id_v)
            break

        if user_data == '3':  # Подробнее
            print("\033[33m\033[40m\033[1m{}".format(vac[1]))
            print("\033[0m\033[33m\033[40m{}".format(''))
            print(data.vacancies[vac[2]].additionally['snippet'])
            print(data.vacancies[vac[2]].url)
            print(data.vacancies[vac[2]].date)
            print(
                f"{data.vacancies[vac[2]].date[8:10]}-{data.vacancies[vac[2]].date[5:7]}-{data.vacancies[vac[2]].date[0:4]}",
                sep=' ')
            print(f"{data.vacancies[vac[2]].date[11:16]} \n")
            repeat_ = 1

        if user_data == '4':  # Показывать с зарплатой выше
            compare = CompareVacancies(data.vacancies[vac[2]])
            salary_min = data.vacancies[vac[2]].salary_average
            print("Показываем вакансии с зарплатой выше ", salary_min)
            repeat_ = 1

        if user_data == '9':  # Удалить вакансию
            list_for_delete.append(vac[0])
            print("Вакансия будет удалена")
            repeat_ = 1

