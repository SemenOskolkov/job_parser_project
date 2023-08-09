from job_parser.classes import HHVacancy, SJVacancy
from job_parser.engine_classes import HH, SuperJob
from job_parser.utils import sorting, get_top


def main():
    site_name = input(f'Ведите название сайта для поиска вакансии (HH или SuperJob): ')
    job_title = input(f'Введите название вакансии: ')
    number_vacancies = int(input(f'Введите количество вакансий: '))
    sort_vacancies = input(f'Отсортировать вакансии по зарплате? (Yes / No): ')

    if site_name == 'HH':
        hh_engine = HH()
        search_word = job_title
        vacancies_count = number_vacancies
        hh_result = hh_engine.get_request(search_word, vacancies_count)
        hh_data = HH.get_connector('job_parser/res_HH.json')
        hh_data.insert(hh_result)
        HHVacancy.filling_list_vacancies('job_parser/res_HH.json')

        if sort_vacancies.lower() == 'yes':
            get_top(sorting(HHVacancy.vacancies), number_vacancies)
        if sort_vacancies.lower() == 'no':
            get_top(HHVacancy.vacancies, number_vacancies)

    if site_name == 'SuperJob':
        sj_engine = SuperJob()
        search_word = job_title
        vacancies_count = number_vacancies
        sj_result = sj_engine.get_request(search_word, vacancies_count)
        sj_data = SuperJob.get_connector('job_parser/res_SJ.json')
        sj_data.insert(sj_result)
        SJVacancy.filling_list_vacancies('job_parser/res_SJ.json')

        if sort_vacancies.lower() == 'yes':
            get_top(sorting(SJVacancy.vacancies), number_vacancies)
        if sort_vacancies.lower() == 'no':
            get_top(SJVacancy.vacancies, number_vacancies)


if __name__ == '__main__':
    main()
