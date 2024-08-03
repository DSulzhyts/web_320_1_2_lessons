class MarksController:
    def __init__(self, model):
        self.model = model

    def default_action(self):
        if self.model.get_marks():
            return self.model.get_marks()
        else:
            return "Нет данных!"

    def only_courses_list(self):
        courses = []
        data = self.model.get_marks()
        if data:
            for element in data:
                courses.append(element['course'])
        else:
            return "Предметов нет!"
        return courses

    def only_marks_list(self):
        marks = []
        data = self.model.get_marks()
        if data:
            for element in data:
                marks.append(element['mark'])
        else:
            return "Оценок нет!"
        return marks

    def courses_marks(self):
        if self.model.get_marks():
            return self.only_courses_list(), self.only_marks_list()
        else:
            return "Предметов нет! Оценок нет!"

    def add_mark(self, course, mark, filename, validation):
        if validation in ['is_superuser', 'is_staff']:
            self.model.add_mark(course, mark, filename)
            return "Оценка успешно добавлена!"
        else:
            return "Нет доступа!"
