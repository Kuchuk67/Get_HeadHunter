from src.file_vacancies import Files_Vacancies
import json
import typing
from src.vacancy import Vacancy

class FilesJSON(Files_Vacancies):
    """ класс работы  с файлами JSON """



    def data_json_created(self, list_object):
        """ Создает из списка объектов Vacansy список словарей для JSON файла"""
        dict_object = []

        try:
            if typing.TYPE_CHECKING:
                from _typeshed import SupportsRead
                files: SupportsRead[str | bytes]
            with open(self.file_name, encoding='utf-8') as files:
                dict_object = json.load(files)
        except:
            self.remove()

        # Проверка на одинаковые вакансии

        for object_ in list_object:
            er = 0
            for d_o in dict_object:
                if d_o.get('_Vacancy__id_v') == str(object_.id_v):
                    er = 1
                    break
            if er != 1:
                dict_object.append(
                {
                    "_Vacancy__id_v": object_.id_v,
                    "_Vacancy__name": object_.name,
                    "_Vacancy__salary_from": object_.salary_from,
                    "_Vacancy__salary_to": object_.salary_to,
                    "_Vacancy__salary_average": object_.salary_average,
                    "_Vacancy__url": object_.url,
                    "_Vacancy__currency": object_.currency,
                    "_Vacancy__date": object_.date,
                    "_Vacancy__additionally": object_.additionally
                }
                )
        return dict_object


    def save(self, dict_object) -> str:
        """ Добавляет вакансии в файл """


        if typing.TYPE_CHECKING:
            from _typeshed import SupportsWrite
            files: SupportsWrite[str]
        try:
            with open(self.file_name, 'w', encoding='utf-8' ) as files:
                json.dump(dict_object, fp=files, indent=4, ensure_ascii=False)
        except Exception as er:
            return f"Ошибка записи файла; {er}"
        else:
            return 'Ok'


    def read(self):
        """ Читает вакансии из файла """
        if typing.TYPE_CHECKING:
            from _typeshed import SupportsRead
            files: SupportsRead[str | bytes]

        with open(self.file_name, encoding='utf-8') as files:
            data = json.load(files)

        return data
            # из JSON создать  список объектов
        #del self.vacancies
