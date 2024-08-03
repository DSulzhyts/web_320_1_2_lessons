import pytest

from module_08_OOP.OOP_test._11_abstractions import Employer


@pytest.fixture
def employer():
    Employer.employers_dict.clear()
    employer = Employer("test_name", "test_surname", "test_phone")
    return employer
