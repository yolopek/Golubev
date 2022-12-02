import csv
import re
import sys
from var_dump import var_dump

class DataSet:
    """Класс для представления массива вакансий по имени файла

    Attributes:
        file_name (str): Название файла
        vacancies_objects (array): Массив вакансий
    """
    def __init__(self, file_name, vacancies_objects):
        """Инициализирует объект DataSet

        Args:
            file_name (str): Название файла
            vacancies_objects (array): Массив вакансий
        """
        self.file_name = file_name
        self.vacancies_objects = vacancies_objects
        
class Vacancy:
    """Класс для представления вакансии

        Attributes:
            name(str): Название вакансии
            description(str): Описание вакансии
            key_skills(str): Ключевые навыки
            experience_id(int or float): Опыт работы
            premium(bool): Наличие премии у вакансии
            employer_name(str): Имя работодателя
            salary(int): Возможная зарплата
            area_name(str): Расположение вакансии
            published_at(datetime): Дата публикации вакансии
    """
    def __init__(self, name, description, key_skills, experience_id, premium, employer_name, salary, area_name, published_at):
        """Инициализирует объект Vacancy

        Args:
            name(str): Название вакансии
            description(str): Описание вакансии
            key_skills(str): Ключевые навыки
            experience_id(int or float): Опыт работы
            premium(bool): Наличие премии у вакансии
            employer_name(str): Имя работодателя
            salary(int): Возможная зарплата
            area_name(str): Расположение вакансии
            published_at(datetime): Дата публикации вакансии
        """
        self.name = name
        self.description = description
        self.key_skills = key_skills
        self.experience_id = experience_id
        self.premium = premium
        self.employer_name = employer_name
        self.salary = salary
        self.area_name = area_name
        self.published_at = published_at

class Salary:
    """Класс для представления зарплаты
    
        Attributes:
            salary_from(int): Нижняя граница зарплаты
            salary_to(int): Верхняя граница зарплаты
            salary_gross(bool)
            salary_currency(str): Валюта зарплаты
    """
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        """Инициализирует объект Salary

        Args:
            salary_from(int): Нижняя граница зарплаты
            salary_to(int): Верхняя граница зарплаты
            salary_gross(bool)
            salary_currency(str): Валюта зарплаты
        """
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_gross = salary_gross
        self.salary_currency = salary_currency

def csv_reader(file_name):
    """Считывает назваение файла и разделяет содержимое на массив заголовков и на массив данных

    Returns:
        headers(array): Массив заголовков
        data(array): Массив данных
    """
    data = []
    with open(file_name, encoding='utf-8-sig') as r_file:
        file_reader = csv.reader(r_file)
        headers = next(file_reader)
        lines = list(file_reader)
        for i in lines:
            list_files = [x for x in i if x != '']
            if (len(list_files) == len(headers)):
                data.append(list_files)
    return headers, data

def input_correct():
    """Принимает название файла и параметры от пользователя для фильтрации данных

    Returns:
        file_name(str): название файла
        filter_name(str): название фильтра
        filter_value(str): величина фильтра
        sort_param(str): параметр сортировки
        sord_order(str): порядок сортировки
        ranges(str): диапазон сортировки
        colums(str): требуемые столбцы
    """
    file_name = input("Введите название файла: ")
    filter_param = input("Введите параметр фильтрации: ")
    sort_param = input("Введите параметр сортировки: ")
    sort_order = input("Обратный порядок сортировки (Да / Нет): ")
    ranges = input("Введите диапазон вывода: ")
    colums = input("Введите требуемые столбцы: ")
    if filter_param != "":
        if filter_param.find(":") == -1:
            print("Данные некорректны!")
            return
        filter_name = filter_param[:filter_param.find(":")]
        filter_value = filter_param[:filter_param.find(":") + 2:]
    else:
        filter_name = ""
        filter_value = ""
    return file_name, filter_name, filter_value, sort_param, sort_order, ranges, colums

def make_parse(file_name):
    """Очищает элементы массива с данными от лишней информации

    Returns:
        vacancies(array): массив с очищенными данными
    """
    result_parse = []
    with open(file_name, encoding='utf_8_sig') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for line in file_reader:
            result_parse.append(line)

    try:
        row_name = result_parse.pop(0)
    except Exception:
        print('Пустой файл')
        sys.exit()

    all_vacancies = []
    for line in result_parse:
        if len(row_name) == len(line) and '' not in line:
            all_vacancies.append(line)

    vacancies = []
    for line in all_vacancies:
        dict_result = {}
        for i in range(0, len(row_name)):
            list_values = []
            if line[i].find('\n') != -1:
                for j in line[i].split("\n"):
                    lines = " ".join(re.sub(r"<[^>]+>", "", j).split())
                    list_values.append(lines)
            else:
                list_values = " ".join(re.sub(r"<[^>]+>", "", line[i]).split())
            dict_result[row_name[i]] = list_values
        vacancies.append(dict_result)
    return vacancies

file_name, filter_name, filter_value, sort_param, sort_order, ranges, colums = input_correct()
data_vacancies = make_parse(file_name)
vacancies_objects = []
for vacancy in data_vacancies:
    salary_object = Salary(vacancy["salary_from"], vacancy["salary_to"], vacancy["salary_gross"], vacancy["salary_currency"])
    vacancy_object = Vacancy(vacancy["name"], vacancy["description"], vacancy["key_skills"], vacancy["experience_id"] ,vacancy["premium"], vacancy["employer_name"], salary_object, vacancy["area_name"], vacancy["published_at"])
    vacancies_objects.append(vacancy_object)

var_dump(DataSet(file_name, vacancies_objects))






