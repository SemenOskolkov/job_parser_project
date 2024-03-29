## Парсинг вакансий с сайтов HH и SuperJob

### Описание проекта

Проект представляет собой парсинг вакансий с сайтов HH и SuperJob с применением объектно-ориентированного программирования.

Поиск вакансии запускается с помощью скрипта, прописанного в файле **pyproject.toml**

### Содержание проекта

Директория **"job_parser"** :

**"classes.py"** - файл с классами по работе с вакансиями;

**"connector.py"** - файл по работе с json файлами;

**"engine_classes.py"** - файл с классами для подключения API;

**"main.py"** - файл с основным телом программы;

**"utils.py"** - файл с функциями

**"res_HH.json"** - файл с данными вакансий сайта Head Hunter

**"res_SJ.json"** - файл с данными вакансий сайта Super Job

### Основные системные требования:

* Python ^3.10
* Poetry 0.1.0

### Установка необходимого ПО

#### Установка Poetry

https://python-poetry.org/docs/

#### проверка версии Poetry

```
poetry --version
```

### Запуск проекта

1. Загрузите проект из Github в директорию, воспользовавшись командой

```
git clone git@github.com:SemenOskolkov/job_parser_project.git
```
2. Перейдите в директорию проекта **job_parser_project**;

```
cd job_parser_project
```

3. Активируйте виртуальное окружение

```
poetry shell
```

4. Запустите поиска вакансий через терминал используя команду

```
poetry run find_job
```

Чтобы выйти из виртуального окружения, используйте команду

```
exit
```

### Ввод данных после запуска команды поиска вакансий:

1. Введите название сайта для поиска вакансии (HH или SuperJob) и нажмите **Enter**. 

```
Ведите название сайта для поиска вакансии (HH или SuperJob):
```
2. Введите название вакансии и нажмите **Enter**. 

```
Введите название вакансии:
```
3. Введите количество вакансий которое хотите получить в результате и нажмите **Enter**. 

```
Введите количество вакансий: 
```
4. Введите **Yes**, если желаете отсортировать вакансии по зарплате или **No**, если не желаете и нажмите **Enter**. 

```
Отсортировать вакансии по зарплате? (Yes / No):
```

ПРИМЕР
```
Ведите название сайта для поиска вакансии (HH или SuperJob): HH
Введите название вакансии: Python разработчик
Введите количество вакансий: 15
Отсортировать вакансии по зарплате? (Yes / No): yes
 
```
