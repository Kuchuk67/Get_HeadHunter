from src.vacancy import Vacancy


class Vacancies:
    """Формирует из данных полученных по API  список с объектами вакансий,
добавляет объекты, сортирует список, удаляет объекты из списка"""

    def __init__(self) -> None:
        self.__vacancies: list = []

    @property
    def vacancies(self) -> list:
        """ Возвращает список экземпляров вакансия Vacancу"""
        return self.__vacancies


    def created(self, x: list) -> None:

        """ Создает список объектов с вакансиями"""
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
    def vacancies(self, data: Vacancy) -> None:
        """ Добавляет в список экземпляров вакансию Vacancу"""
        self.__vacancies.append(data)

    @vacancies.deleter
    def vacancies(self) -> None:
        """ Удаляет все вакансии"""
        self.__vacancies = []

    def vacancy_del(self, id_v: int) -> bool:
        """ Удаляет  вакансию"""

        for index, object_vacancy in enumerate(self.vacancies):
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
    """ Возвращает следующее объект Вакансию Vacancy.
        Returns:
            int: Следующая ваканси.
        Raises:
            raise StopIteration: Если достигнута верхняя граница диапазона.
        """

    def __init__(self, vacancies: list) -> None:
        self.vacancies = vacancies
        self.step = 0

    def __next__(self) -> tuple[int, str, int]:
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

    def __iter__(self) -> object:
        return self
