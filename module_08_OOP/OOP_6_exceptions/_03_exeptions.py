class MyZeroDivision(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivision("очень плохие новости!")
    else:
        raise ZeroDivisionError("плохие новости!")


for mode in [True, False]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print("Деление на ноль!")

for mode in [True, False]:
    try:
        do_the_division(mode)
    except MyZeroDivision as mZD:
        print(mZD)
    except ZeroDivisionError as ZD:
        print(ZD)
