def len_vac(data):
    # if data.vacansies:
    print(f"В списке загружено вакансий: {len(data.vacancies)}")


def menu(data):
    print("\n--- МЕНЮ --- \n1. Загрузить вакансии")
    if len(data.vacancies) > 0:
        print("2. Сортировать список по дата\n3. Сортировать список по зарплате")
        print("4. Просмотр списка вакансий\n8. Удалить список вакансий")
        # print("8. Удалить список вакансий")
    print("0. Выход\n")
    user_input = input("Выберите пункт меню: ")
    return user_input