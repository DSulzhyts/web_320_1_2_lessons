from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        pass


def singleton_test(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    print("Если вы видите то же значение, одиночка был переиспользован (УАУ!)\n"
          "Если вы видите разные значения, тогда было создано 2 одиночки (ФУУУ!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=singleton_test, args=("FOO",))
    process2 = Thread(target=singleton_test, args=("BAR",))
    process1.start()
    process2.start()
