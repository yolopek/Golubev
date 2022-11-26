import csv
import re
import datetime
import sys
import os
from prettytable import PrettyTable

clean_items = re.compile('<.*?>')
def clean_html(raw_html):
    clean_text = re.sub(clean_items, '', raw_html).replace('\n', ', ').replace('\r\n', ' ').strip()
    clean_text = re.sub(" +", ' ', clean_text)
    clean_text = ' '.join(clean_text.split())
    return clean_text

def csv_reader(file_name):
    data = []
    with open(file_name, encoding='utf-8-sig') as r_file:
        file_reader = csv.reader(r_file)
        headers = next(file_reader)
        lines = list(file_reader)
        for i in lines:
            list_files = [x for x in i if x != '']
            if (len(list_files) == len(headers)):
                data.append(list_files)

    if (len(data) == 0):
        print('Нет данных')
        sys.exit()
    return headers, data

def formatter(line, headers):
    income_info = ''
    refactor_line = []
    for i in range(0, len(headers)):
        line[i] = clean_html(line[i])
        if (i == 3):
            refactor_line.append(experience[line[i]])
        elif (i == 4):
            if (line[i] == 'FALSE' or line[i] == 'False'):
                refactor_line.append('Нет')
            elif (line[i] == 'TRUE' or line[i] == 'True'):
                refactor_line.append('Да')
        elif (5 < i < 10):
            if (i == 6):
                first_number = '{0:,}'.format(int(float(line[i]))).replace(',', ' ')
                second_number = '{0:,}'.format(int(float(line[i + 1]))).replace(',', ' ')
                income_info = f'{(first_number)} - {second_number} ({currencies[line[i + 3]]}) '
            if (i == 8):
                if (line[i] == 'FALSE' or line[i] == 'False'):
                    income_info += '(С вычетом налогов)'
                elif (line[i] == 'TRUE' or line[i] == 'True'):
                    income_info += '(Без вычета налогов)'
            if (i == 9):
                refactor_line.append(income_info)
        elif (i == 9):
            refactor_line.append(currencies[line[i]])
        elif (i == 11):
            refactor_line.append(datetime.datetime.strptime(line[i][:10], "%Y-%m-%d").strftime("%d.%m.%Y"))
        else:
            refactor_line.append(line[i])
    return refactor_line

def csv_filer(headers, data):
    headers_refactor = []
    for index in range(len(headers)):
        if (index == 6):
            headers_refactor.append('salary')
        elif (headers[index] != 'salary_from' and headers[index] != 'salary_to'
              and headers[index] != 'salary_gross' and headers[index] != 'salary_currency'):
            headers_refactor.append(headers[index])

    refactor_data = []
    for line in data:
        refactor_data.append(formatter(line, headers))

    return headers_refactor, refactor_data

def table_vacancies(headers, data):
    table = PrettyTable()
    field_names = ['№']
    for names in headers:
        field_names.append(main_names[names])

    table.field_names = field_names
    table.hrules = 1
    table.align = 'l'
    table.max_width = 20;

    number_line = 1
    for i in range(len(data)):
        row = [str(number_line)]
        format_line = []
        for j in range (len(data[i])):
            if (len(data[i][j]) > 100):
                if (j == 2):
                    format_line.append(data[i][j].replace(", ", "\n")[:100] + "...")
                else:
                    format_line.append(data[i][j][:100] + "...")
            else:
                if (j == 2):
                    format_line.append(data[i][j].replace(", ", "\n"))
                else:
                    format_line.append(data[i][j])
        row.extend(format_line)
        table.add_row(row)
        number_line += 1

    return table

main_names = dict({'name': 'Название', 'description' : 'Описание', 'key_skills': 'Навыки',
                   'experience_id': 'Опыт работы', 'premium': 'Премиум-вакансия', 'employer_name': 'Компания',
                   'salary': 'Оклад',
                   'area_name': 'Название региона', 'published_at': 'Дата публикации вакансии'})

experience = dict({"noExperience": "Нет опыта", "between1And3": "От 1 года до 3 лет",
                   "between3And6": "От 3 до 6 лет", "moreThan6": "Более 6 лет"})

currencies = dict({"AZN": "Манаты", "BYR": "Белорусские рубли", "EUR": "Евро", "GEL": "Грузинский лари",
                   "KGS": "Киргизский сом", "KZT": "Тенге", "RUR": "Рубли", "UAH": "Гривны", "USD": "Доллары",
                   "UZS": "Узбекский сум"})

file = input()
numbers_rows = input().split(' ')
name_rows = input().split(', ')
file_pycharm = "vacancies_medium.csv"

if (os.stat(file).st_size == 0):
    print("Пустой файл")
    sys.exit()

main_headers, main_data = csv_reader(file)

main_headers_refactor, main_refactor_data = csv_filer(main_headers, main_data)

table = table_vacancies(main_headers_refactor, main_refactor_data)

if (numbers_rows[0] == ''):
    if (name_rows[0] == ''):
        print(table)
    else:
        table = table.get_string(fields = ['№'] + name_rows)
        print(table)
    sys.exit()


if (len(numbers_rows) == 2):
    if (name_rows[0] != ''):
        table = table.get_string(start=int(numbers_rows[0]) - 1, end=int(numbers_rows[1]) - 1, fields=['№'] + name_rows)
    else:
        table = table.get_string(start=int(numbers_rows[0]) - 1, end=int(numbers_rows[1]) - 1)
elif (len(numbers_rows) == 1):
    if (name_rows[0] != ''):
        table = table.get_string(start=int(numbers_rows[0]) - 1, fields=['№'] + name_rows)
    else:
        table = table.get_string(start=int(numbers_rows[0]) - 1)

print(table)

