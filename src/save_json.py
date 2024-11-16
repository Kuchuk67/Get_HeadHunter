from src.abc_save import Save_Vacancies
import json
import typing

from src.vacancy import Vacancy


class SaveJSON(Save_Vacancies):

    ''' обслуживание ввода-вывода JSON файлов '''
    def __init__(self,file_name:str):
        #self.vacancies = []
        super().__init__(file_name)

    @staticmethod
    def data_json(list_object):
        ''' Создает из списка объектов список словарей для JSON файла'''
        dict_object = []
        for  object_ in list_object:
            dict_object.append(object_.__dict__)

        #return json.dumps(dict_object, indent=4, ensure_ascii=False )
        return dict_object

    def save(self):
        dict_object = []
        for object_ in self.vacancies:
            #dict_ = object_.__dict__
            #dict_ = {k: unicode(v).encode("utf-8") for k, v in dict_.iteritems()}
            dict_object.append(object_.__dict__)


        #d['quote_text'].encode("ascii", "ignore").decode('utf-8')

        if typing.TYPE_CHECKING:
            from _typeshed import SupportsWrite
            files: SupportsWrite[str]

        with open(self.file_name, 'w', encoding='utf-8' ) as files:
            json.dump(dict_object, fp=files, indent=4, ensure_ascii=False)


    def read(self):
        if typing.TYPE_CHECKING:
            from _typeshed import SupportsRead
            files: SupportsRead[str | bytes]

        with open(self.file_name, encoding='utf-8') as files:
            data = json.load(files)

        # print(data)
        # из JSON создать  список объектов
        del self.vacancies
        for dict_vacancy in data:
            #print(',', dict_vacancy)
            try:
                self.vacancies = Vacancy(
                    dict_vacancy.get('_Vacancy__id_v'),
                     dict_vacancy.get('_Vacancy__name'),
                     dict_vacancy.get('_Vacancy__salary_from'),
                     dict_vacancy.get('_Vacancy__salary_to'),
                     dict_vacancy.get('_Vacancy__currency'),
                     dict_vacancy.get('_Vacancy__address'),
                     dict_vacancy.get('_Vacancy__url'),
                     dict_vacancy.get('_Vacancy__snippet'),
                     dict_vacancy.get('_Vacancy__schedule') ,
                    dict_vacancy.get('_Vacancy__date')    )
            except ValueError as txt:
                print(f"Вакансия не добавлена: {txt}")




