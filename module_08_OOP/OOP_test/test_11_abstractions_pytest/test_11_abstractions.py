from module_08_OOP.OOP_test._11_abstractions import Employer


def test_employer_init():
    employer = Employer('test_name', 'test_surname', '12345')
    assert len(Employer.employers_dict) == 1
    assert Employer.employers_dict == {'12345': ['test_name', 'test_surname']}


def test_get_name(employer):
    assert employer.get_name() == "test_name"


def test_get_surname(employer):
    assert employer.get_surname() == "test_surname"


def test_get_phone(employer):
    assert employer.get_phone() == "test_phone"


def test_pay_salary(employer):
    assert employer.pay_salary(1500) == "Работник test_name test_surname, получил зарплату 1500"


def test_print_employers_data(employer):
    assert employer.print_employers_data() == "Данные успешно получены!"
    assert Employer.print_employers_data() == "Данные успешно получены!"


def test_fire_employer(employer):
    print(len(Employer.employers_dict))
    assert employer.fire_employer() == "Сотрудник  test_name, test_surname был уволен!"
    assert employer.fire_employer() == "Сотрудника test_name, test_surname уже уволили!"
    assert len(Employer.employers_dict) == 0

