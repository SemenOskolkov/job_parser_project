import json


class Vacancy:
    __slots__ = ('name', 'link', 'description', 'salary')

    def __init__(self, name, link, description, salary):
        self.name = name
        self.link = link
        self.description = description
        self.salary = salary

    def __str__(self):
        return f'{self.name}, {self.link}, {self.description}, {self.salary}'

    def __repr__(self):
        return f'{self.name}, {self.link}, {self.description}, {self.salary}'



class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __init__(self, data_file):
        name = data_file.get("name")
        link = data_file.get("url")
        description = data_file["snippet"].get("responsibility")
        salary = data_file["salary"].get("from")

        super().__init__(name, link, description, salary)

        try:
            self.salary = data_file["salary"].get("from")
        except AttributeError as e:
            self.salary = 0
            print(e)

    def __lt__(self, other):
        return self.salary < other.salary

    def __str__(self):
        return f'HH: {self.company_name}, зарплата: {self.salary} руб/мес'

    def __repr__(self):
        return f'HH: {self.company_name} {self.salary}'




class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __init__(self, data_file):
        name = data_file.get("profession")
        link = data_file["client"].get("link")
        description = data_file.get("candidat")
        salary = data_file.get("payment_from")

        super().__init__(name, link, description, salary)

        self.salary: float

    def __lt__(self, other):
        return self.salary < other.salary

    def __str__(self):
        return f'SJ: {self.company_name} зарплата: {self.salary} руб.мес'

    def __repr__(self):
        return f'SJ: {self.company_name} зарплата: {self.salary}'

#Общий документ
def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass


# if __name__ == '__main__':
#     with open('result.json', 'r', encoding='utf-8') as f:
#         files = json.load(f)