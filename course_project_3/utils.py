def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    for i in range(top_count):
        print(vacancies[i])
