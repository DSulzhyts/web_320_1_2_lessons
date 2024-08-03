class SushiError(Exception):
    def __init__(self, sushi, message):
        super().__init__(message)
        self.sushi = sushi


class TooFewRiceError(SushiError):
    def __init__(self, sushi, rice, message):
        super().__init__(sushi, message)
        self.rice = rice


class TooMuchRiceError(SushiError):
    def __init__(self, sushi, rice, message):
        super().__init__(sushi, message)
        self.rice = rice


def make_sushi(sushi, rice):
    if sushi not in ['california', 'philadelphia', 'yamato']:
        raise SushiError(sushi, "Позиции нет в меню!")
    if rice < 50:
        raise TooFewRiceError(sushi, rice, "Слишком мало риса!")
    elif rice > 100:
        raise TooMuchRiceError(sushi, rice, "Слишком много риса!")

    return "Ваши суши готовы"


for (sushi, rice) in [('bismark', 70), ('california', 0), ('philadelphia', 75), ('yamato', 110), ('bismark', 0)]:
    try:
        print(make_sushi(sushi, rice))
    except TooFewRiceError as tfre:
        print(f"{tfre}: {tfre.sushi}, {tfre.rice}")
    except TooMuchRiceError as tmre:
        print(f"{tmre}: {tmre.sushi}, {tmre.rice}")
    except SushiError as se:
        print(f"{se}: {se.sushi}")
