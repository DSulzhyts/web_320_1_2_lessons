class Employee:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname


class TimeSheetReport:

    @staticmethod
    def print_time_sheet_report(employee_obj):
        return f"Сотрудник {employee_obj.get_name()} печатает отчет"


employee = Employee("Дмитрий")
print(TimeSheetReport.print_time_sheet_report(employee))
