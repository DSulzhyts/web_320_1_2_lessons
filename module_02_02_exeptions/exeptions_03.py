try:
    raise Exception
except Exception:
    print("Хмм... что-то пошло не так((")
except ValueError:
    print("Получено нужное исключение!")

try:
    raise ValueError
except Exception:
    print("Хмм... что-то пошло не так((")
except ValueError:
    print("Получено нужное исключение!")

try:
    raise ValueError
except ValueError:
    print("Получено нужное исключение!")
except Exception:
    print("Хмм... что-то пошло не так((")


try:
    raise Exception
except ValueError:
    print("Получено нужное исключение!")
except Exception:
    print("Хмм... что-то пошло не так((")