from src.vacancy import Vacancy


class Vacancies():
    """Формирует из данных полученных по API  список с объектами вакансий,
добавляет объекты, сортирует список, удаляет объекты из списка"""

    def __init__(self):
        self.__vacancies = []

    @property
    def vacancies(self):
        return self.__vacancies

    @property
    def len_vacancies(self):
        return len(self.__vacancies)

    def created(self, x: list) -> list:

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

    def vacancy_del(self, id_v) -> bool:
        """Удаляет  вакансию"""

        for index, object_vacancy in enumerate(self.vacancies):
            # print(index," - ",object_vacancy.id_v)
            if int(object_vacancy.id_v) == int(id_v):
                del self.vacancies[index]
                return True
        return False

    def sort_date(self) -> None:
        """ Сортирует список вакансий по дате """
        sort_vacancies = sorted(self.vacancies, key=lambda x: x.date, reverse=True)
        self.__vacancies = sort_vacancies

    def sort_salary(self) -> None:
        """ Сортирует список вакансий по зарплате """
        sort_vacancies = sorted(self.vacancies, key=lambda x: x.salary_average, reverse=True)
        self.__vacancies = sort_vacancies


class IterVacancies:
    """Возвращает следующее объект Вакансию Vacancy.
        Returns:
            int: Следующая ваканси.
        Raises:
            raise StopIteration: Если достигнута верхняя граница диапазона.
        """

    def __init__(self, vacancies):
        self.vacancies = vacancies
        self.step = 0

    def __next__(self):
        try:
            vacancy = self.vacancies[self.step]
        except IndexError:
            raise StopIteration

        self.step += 1
        adress = ""
        if vacancy.additionally['address']:
            adress = f", адрес: {vacancy.additionally['address']}"
        return_value = (vacancy.id_v, f"{vacancy.name}, зарплата: {vacancy.salary_average}, "
                                      f"{vacancy.additionally['schedule']}{adress}", self.step - 1 )
        return return_value

    def __iter__(self):
        return self
