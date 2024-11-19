
from src.get_api import GetAPI


def main():


    x = GetAPI('бухгалтер')
    #x.load_vacancies('бухгалтер')
    print(x.status)
    print(x.vacancies_data)
    #print(x.vacancies)






if __name__ == "__main__":
    main()