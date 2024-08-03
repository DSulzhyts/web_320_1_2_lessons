class MarksView:
    def __init__(self, controller):
        self.controller = controller

    def print_default_action(self):
        print(self.controller.default_action())

    def print_courses_list(self):
        print(self.controller.only_courses_list())

    def print_marks_list(self):
        print(self.controller.only_marks_list())

    def print_courses_marks(self):
        print(self.controller.courses_marks())

    def add_mark(self, course, mark, filename, validation='user'):
        # if validation in ['is_superuser', 'is_staff']:
        #     self.controller.add_mark(course, mark, filename, validation)
        #     print("Оценка успешно добавлена!")
        # else:
        #     print("Нет доступа!")

        print(self.controller.add_mark(course, mark, filename, validation=validation))
