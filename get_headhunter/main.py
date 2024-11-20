
from src.get_api import GetAPI


def main():


    data_ = GetAPI('бухгалтер')
    #x.load_vacancies('бухгалтер')
    print(data_.status)
    print(data_.vacancies_data)
    #print(data_.vacancies)






if __name__ == "__main__":
    main()