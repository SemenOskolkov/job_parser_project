import json


class Vacancy:
    __slots__ = ('name_vacancy', 'link', 'description', 'salary')

    def __init__(self, name_vacancy, link, description, salary):
        self.name_vacancy = name_vacancy
        self.link = link
        self.description = description
        self.salary = salary

    # def __str__(self):
    #     return f'Вакансия: {self.name_vacancy};\nСсылка на вакансию: {self.link};\nОписание вакансии: {self.description};\nЗарплата: {self.salary} руб.'

    def __repr__(self):
        if self.salary:
            return f'Вакансия: {self.name_vacancy};\nСсылка на вакансию: {self.link};\nОписание вакансии: {self.description};\nЗарплата: {self.salary} руб.'
        else:
            return f'Вакансия: {self.name_vacancy};\nСсылка на вакансию: {self.link};\nОписание вакансии: {self.description};\nЗарплата: не указана.'

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __iter__(self):
        self.value = 0
        return self.value

    def __next__(self):
        if self.value < self.count:
            self.value += 1
        else:
            raise StopIteration


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(self.data_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                return len(item)


class HHVacancy(CountMixin, Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    data_file = 'res_HH.json'
    vacancies = []

    def __init__(self, name, link, description, salary, company_name):
        super().__init__(name, link, description, salary)
        self.company_name = company_name
        self.count = CountMixin.get_count_of_vacancy

    @classmethod
    def filling_list_vacancies(cls, data_file):
        with open(f'{data_file}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                name_vacancy_hh = item.get("name")
                link_hh = item.get("url")
                description_hh = item["snippet"].get("responsibility")
                company_name_hh = item['employer'].get('name')
                try:
                    salary_hh = item["salary"].get("from")
                    if salary_hh is None:
                        salary_hh = 0
                except AttributeError:
                    salary_hh = 0
                cls.vacancies.append(HHVacancy(name_vacancy_hh, link_hh, description_hh, salary_hh, company_name_hh))

    def __repr__(self):
        return f'HH: Название компании: {self.company_name} ' + super().__repr__()


class SJVacancy(CountMixin, Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    data_file = 'res_SJ.json'
    vacancies = []

    def __init__(self, name, link, description, salary, company_name):
        super().__init__(name, link, description, salary)
        self.count = CountMixin.get_count_of_vacancy
        self.company_name = company_name
        print(self.count)

    @classmethod
    def filling_list_vacancies(cls, data_file):
        with open(f'{data_file}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                name_vacancy_sj = item.get("profession")
                link_sj = item["client"].get("link")
                description_sj = item.get("candidat")
                company_name_sj = item["client"].get("title")
                try:
                    salary_sj = item.get("payment_from")
                    if salary_sj is None:
                        salary_sj = 0
                except AttributeError:
                    salary_sj = 0
                cls.vacancies.append(SJVacancy(name_vacancy_sj, link_sj, description_sj, salary_sj, company_name_sj))

    def __repr__(self):
        return f'HH: Название компании: {self.company_name} ' + super().__repr__()

# if __name__ == '__main__':
# print(HHVacancy.filling_list_vacancies('res_HH.json'))
# sort_list = sorting(HHVacancy.vacancies)
# get_top(sort_list, 7)
# HHVacancy.get_count_of_vacancy

# print(SJVacancy.filling_list_vacancies('res_SJ.json'))
# sort_list = sorting(SJVacancy.vacancies)
# get_top(sort_list, 10)
# print(SJVacancy.get_count_of_vacancy)
