from unittest import TestCase
from GolubevAT18 import Vacancy, Salary

salary = Salary('10', '24', 'False', 'RUR')

class VacancyTests(TestCase):
    def test_vacancy_type(self):
        self.assertEqual(type(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300')).__name__, 'Vacancy')
    def test_vacancy_name(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300').name, 'Программист')
    def test_vacancy_key_skills(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300').key_skills, 'Ответственность')
    def test_vacancy_experience_id(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300').experience_id, '5')
    def test_vacancy_premium(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300').premium, 'True')
    def test_vacancy_employer_name(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300').employer_name, 'Контур')
    def test_vacancy_salary(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      salary, 'Челябинск', '2022-07-06T00:15:41+0300').salary, salary)
    def test_vacancy_area_name(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300').area_name, 'Челябинск')
    def test_vacancy_published_at(self):
        self.assertEqual(Vacancy('Программист', 'Описание профессии', 'Ответственность', '5', 'True', 'Контур',
                                      Salary('10', '24', 'False', 'RUR'), 'Челябинск', '2022-07-06T00:15:41+0300').published_at, '2022-07-06T00:15:41+0300')