from unittest import TestCase
from GolubevAT18 import Salary

class SalaryTests(TestCase):
    def test_salary_type(self):
        self.assertEqual(type(Salary('10', '24', 'False', 'RUR')).__name__, 'Salary')
    def test_salary_from(self):
        self.assertEqual(Salary('10', '24', 'False', 'RUR').salary_from, '10')
    def test_salary_to(self):
        self.assertEqual(Salary('10', '24', 'False', 'RUR').salary_to, '24')
    def test_salary_gross(self):
        self.assertEqual(Salary('10', '24', 'False', 'RUR').salary_gross, 'False')
    def test_salary_currency(self):
        self.assertEqual(Salary('10', '24', 'False', 'RUR').salary_currency, 'RUR')