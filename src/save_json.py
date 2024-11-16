from src.abc_save import Save_Vacancies
import json
import typing

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
            dict_object.append(object_.__dict__)

        if typing.TYPE_CHECKING:
            from _typeshed import SupportsWrite
            files: SupportsWrite[str]

        with open(self.file_name, 'w') as files:
            json.dump(dict_object, fp=files, indent=4, ensure_ascii=False)


    def read(self):
        if typing.TYPE_CHECKING:
            from _typeshed import SupportsRead
            files: SupportsRead[str | bytes]

        with open(self.file_name) as files:
            data = json.load(files)

        print(data)



    def remove(self):
        pass