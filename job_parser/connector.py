import json
import os


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        """
        try:
            file = open(self.__data_file, 'r', encoding='utf-8')
        except FileNotFoundError:
            file = open(self.__data_file, 'w', encoding='utf-8')
            data = []
            json.dump(data, file, ensure_ascii=False)
        else:
            data = json.load(file)
            print(data)
        finally:
            file.close()

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        file = open(self.__data_file, 'r', encoding='utf-8')
        new_data = json.load(file)
        for item in data:
            new_data.append(item)
        file.close()

        file = open(self.__data_file, 'w', encoding='utf-8')
        json.dump(new_data, file, ensure_ascii=False)
        file.close()

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        file = open(self.__data_file, 'r', encoding='utf-8')
        data = json.load(file)
        file.close()

        if not len(query):
            return data

        query_data = []
        for k in data[query.keys()]:
            if data[k] == query.values():
                query_data.append(data[k])

        return query_data

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """
        if not len(query): return

        file = open(self.__data_file, 'r', encoding='utf-8')
        data = json.load(file)
        file.close()

        count = 0
        for k in data:
            if k.get(list(query.keys())[0]) == list(query.values())[0]:
                del data[count]
            count += 1

        file = open(self.__data_file, 'w', encoding='utf-8')
        json.dump(data, file, ensure_ascii=False)
        file.close()

        return


if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select({'id': 1})
    assert data_from_file == [data_for_file]

    df.delete(dict())
    data_from_file = df.select(dict())
    assert data_from_file == []
