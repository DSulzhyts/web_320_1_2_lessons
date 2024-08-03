from module_08_OOP.OOP_6_exceptions._04_exeptions import make_sushi, SushiError, TooFewRiceError, TooMuchRiceError
import pytest


def test_make_sushi():
    assert make_sushi('philadelphia', 75) == 'Ваши суши готовы'
    with pytest.raises(SushiError):
        make_sushi('bismark', 70)
    with pytest.raises(TooFewRiceError):
        make_sushi('yamato', 40)
    with pytest.raises(TooMuchRiceError):
        make_sushi('philadelphia', 110)
