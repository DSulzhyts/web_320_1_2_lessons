import json


class MarksModel:

    def __init__(self):
        self.student_marks = []

    def get_marks(self):
        return self.student_marks

    def add_mark(self, course, mark, filename):
        data = {}
        data['course'] = course
        data['mark'] = mark
        self.student_marks.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.student_marks, fp, ensure_ascii=False, indent=2)


# if __name__ == "__main__":
#     model = MarksModel()
#     print(model.get_marks())
#     model.add_mark('HTML', 10, 'marks_file.json')
#     model.add_mark('CSS', 12, 'marks_file.json')
#     model.add_mark('JavaScript', 11, 'marks_file.json')
#     model.add_mark('Python', 9, 'marks_file.json')
#     print(model.get_marks())