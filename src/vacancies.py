from src.vacancy import Vacancy


class Vacancies():
    """Формирует из данных полученных по API  список с объектами вакансий,
добавляет объекты, сортирует список, удаляет объекты из списка"""

    def __init__(self):
        self.__vacancies = []
        super().__init__()

    @property
    def vacancies(self):
        return self.__vacancies

    def created(self,x:list) -> list:

        """Отдает список объектов с вакансиями"""
        if self.__vacancies == [] and not x == []:
            for vacancy in x:


                try:
                    self.__vacancies.append(Vacancy(vacancy.get('_Vacancy__id_v'),
                                                    vacancy.get('_Vacancy__name'),
                                                    vacancy.get('_Vacancy__salary_from'),
                                                    vacancy.get('_Vacancy__salary_to'),
                                                    vacancy.get('_Vacancy__currency'),
                                                    vacancy.get('_Vacancy__url'),
                                                    vacancy.get('_Vacancy__date'),
                                                    vacancy.get('_Vacancy__additionally')
                                                    ))
                except ValueError as txt:
                    print(f"Вакансия не добавлена: {txt}")



    @vacancies.setter
    def vacancies(self, data):
        self.__vacancies.append(data)

    @vacancies.deleter
    def vacancies(self):
        """Удаляет все вакансии"""
        self.__vacancies = []
        # del self.vacancies_data

    def vacancy_del(self, id_v) -> None:
        """Удаляет  вакансию"""
        for index, object_vacancy in enumerate(self.vacancies):
            #print(index," - ",object_vacancy.id_v)
            if int(object_vacancy.id_v) == id_v:
                del self.vacancies[index]
                break

    def sort_date(self) -> None:
        """ Сортирует список вакансий по дате """
        sort_vacancies = sorted(self.vacancies, key=lambda x: x.date, reverse=True)
        self.__vacancies = sort_vacancies

    def sort_salary(self) -> None:
        """ Сортирует список вакансий по зарплате """
        sort_vacancies = sorted(self.vacancies, key=lambda x: x.salary_average, reverse=False)
        self.__vacancies = sort_vacancies