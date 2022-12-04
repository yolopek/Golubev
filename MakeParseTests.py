from unittest import TestCase
from GolubevAT18 import make_parse

class MakeParseTests(TestCase):
    def test_parse_null(self):
        self.assertEqual(make_parse("vacancies_null.csv"), "Пустой файл")
