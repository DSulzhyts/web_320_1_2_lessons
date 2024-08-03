class Target:

    def request(self):
        return "Target: Обычное поведение таргета"


class Adaptee:

    def specific_request(self):
        return ".атеграт еинедевоП"


class Adapter(Target, Adaptee):
    def request(self):
        return f'Adapter: (Адаптировано) {self.specific_request()[::-1]}'


def client_code(target: "Target"):
    print(target.request(), end='')


if __name__ == "__main__":
    print("Клиент: Я могу прекрасно работать с объектами Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Клиент: Adaptee имеет странный интерфейс. Я его не могу понять")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Клиент: но я могу работать с ним используя Adapter")
    adapter = Adapter()
    client_code(adapter)

