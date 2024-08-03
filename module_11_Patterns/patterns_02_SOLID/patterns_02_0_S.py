# class Employee:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def print_time_sheet_report(self):
#         return f"Сотрудник {self.__name} печатает отчет"


# employee = Employee("Дмитрий")
# print(employee.print_time_sheet_report())


class Employee:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class TimeSheetReport:

    @staticmethod
    def print_time_sheet_report(employee_obj):
        return f"Сотрудник {employee_obj.get_name()} печатает отчет"


employee = Employee("Дмитрий")
print(TimeSheetReport.print_time_sheet_report(employee))
