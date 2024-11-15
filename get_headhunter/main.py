from src.vacancies import Vacancies

def main():
    x = Vacancies('111.json')
    # del x.vacancies
    x.load_vacancies('бухгалтер')

    print(x.vacancies_data)
    print(x.vacancies)
    for v in x.vacancies:
        print(v.name, ' - ', v.snippet, v.salary_from, '-', v.salary_to, v.currency, v.address, v.schedule, v.url)

    del x.vacancies
    print(x.vacancies)

    print(v.compare_vacancies(v))

if __name__ == "__main__":
    main()