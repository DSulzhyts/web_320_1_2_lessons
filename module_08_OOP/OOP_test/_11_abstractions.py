class Employer:
    employers_dict = {}

    def __init__(self, name, surname, phone):
        self.__name = name
        self.__surname = surname
        self.__phone = phone
        Employer.employers_dict[self.__phone] = [self.__name, self.__surname]

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_phone(self):
        return self.__phone

    def pay_salary(self, salary):
        return f"Работник {self.__name} {self.__surname}, получил зарплату {salary}"

    @staticmethod
    def print_employers_data():
        for phone, data in Employer.employers_dict.items():
            print(data[0])
            print(data[1])
            print(phone)
            print()
            return "Данные успешно получены!"

    def fire_employer(self):
        if self.__phone in Employer.employers_dict.keys():
            self.employers_dict.pop(self.__phone)
            return f"Сотрудник  {self.__name}, {self.__surname} был уволен!"
        else:
            return f"Сотрудника {self.__name}, {self.__surname} уже уволили!"
