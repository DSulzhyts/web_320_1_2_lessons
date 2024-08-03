import unittest
from module_08_OOP.OOP_test._11_abstractions import Employer


class TestEmployer(unittest.TestCase):
    employer = Employer('test_name', 'test_surname', 'test_phone')

    def test_1_init(self):
        self.assertEqual(len(Employer.employers_dict), 1)
        self.assertEqual(Employer.employers_dict, {'test_phone': ['test_name', 'test_surname']})

    def test_2_get_name(self):
        self.assertEqual(self.employer.get_name(), 'test_name')

    def test_3_get_surname(self):
        self.assertEqual(self.employer.get_surname(), 'test_surname')

    def test_4_get_phone(self):
        self.assertEqual(self.employer.get_phone(), 'test_phone')

    def test_5_pay_salary(self):
        self.assertEqual(self.employer.pay_salary(1500), 'Работник test_name test_surname, получил зарплату 1500')

    def test_6_print_employers_data(self):
        self.assertEqual(self.employer.print_employers_data(), "Данные успешно получены!")

    def test_7_fire_employer(self):
        self.assertEqual(self.employer.fire_employer(), "Сотрудник  test_name, test_surname был уволен!")
        self.assertEqual(self.employer.fire_employer(), "Сотрудника test_name, test_surname уже уволили!")
        self.assertEqual(Employer.employers_dict, {})
