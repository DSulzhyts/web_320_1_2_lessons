from abc import ABC, abstractmethod


class Subject(ABC):

    @staticmethod
    def request(self):
        pass


class RealSubject(Subject):

    def request(self):
        print("RealSubject: выполняю запрос")


class Proxy(Subject):

    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Проверка доступа для передачи запроса реальному субъекту")
        return True

    def log_access(self):
        print("Proxy: заношу в лог время запроса")


def client_code(subject: Subject):
    subject.request()


print("Client: исполняю клиентский код с реальным субъектом")
real_subject = RealSubject()
client_code(real_subject)
print("")
print("Client: исполняю тот же клиентский код с заместителем (proxy)")
proxy = Proxy(real_subject)
client_code(proxy)
