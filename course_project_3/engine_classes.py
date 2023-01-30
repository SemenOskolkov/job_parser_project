import json

import requests
from abc import ABC, abstractmethod
from connector import Connector


class Engine(ABC):

    @abstractmethod
    def get_request(self, search_word, vacancies_count):
        return search_word, vacancies_count

    @staticmethod
    def get_connector(file_name):  # Vozvrashaet ekzempliar classsa
        exemplar_conn = Connector(file_name)
        return exemplar_conn


class HH(Engine):
    __url = 'http://api.hh.ru'
    __per_page = 20

    def get_vacancies(self, search_word, page):
        # print(f'Try to get page {page + 1}')
        response = requests.get(f'{self.__url}/vacancies?text={search_word}&page={page}')
        if response.status_code == 200:
            return response.json()
        return None

    def get_request(self, search_word, vacancies_count):
        page = 0
        result = []
        while self.__per_page * page < vacancies_count:
            tmp_result = self.get_vacancies(search_word, page)
            if tmp_result:
                result += tmp_result.get('items')
                page += 1
            else:
                break
        return result


class SuperJob(Engine):
    __url = 'https://api.superjob.ru/2.0'
    __secret = 'v3.r.137222938.adcc1bf5602cc5a2c697d63eb9c580dd5029f96f.049aae965267ebe71bbc7c587187da62cdbc560e'
    __per_page = 20

    def _send_request(self, search_word, page):
        headers = {
            'X-Api-App-Id': self.__secret,
            'Content-Type': 'application / x - www - form - urlencoded'
        }
        response = requests.get(url=f'{self.__url}/vacancies?keyword={search_word}&page={page}', headers=headers)
        if response.status_code == 200:
            # print(f'Try to get page {page + 1}')
            return response.json()
        return None

    def get_request(self, search_word, vacancies_count):
        page = 0
        result = []
        while self.__per_page * page <= vacancies_count:
            tmp_result = self._send_request(search_word, page)
            if tmp_result:
                result += tmp_result.get('objects')
                page += 1
            else:
                break
        return result
