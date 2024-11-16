from src.abc_save import Save_Vacancies
import json

class SaveJSON(Save_Vacancies):
    ''' обслуживание ввода-вывода JSON файлов '''
    def __init__(self,file_name:str):

        super().__init__(file_name)

    @staticmethod
    def data_json(list_object):
        ''' Создает из списка объектов список словарей для JSON файла'''
        dict_object = []
        for  object in list_object:
            dict_object.append(object.__dict__)
        json_data = json.dumps(dict_object, indent=4, ensure_ascii=False )
        return json_data

    def save(self):
        pass

    def read(self):
        pass

    def remove(self):
        pass