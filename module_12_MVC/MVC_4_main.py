from MVC_1_Model import MarksModel
from MVC_2_View import MarksView
from MVC_3_Controller import MarksController

model = MarksModel()
controller = MarksController(model)
view = MarksView(controller)

view.print_default_action()
view.print_courses_list()
view.print_marks_list()
view.print_courses_marks()
view.add_mark('HTML', 10, 'marks_file.json', 'is_staff')
view.add_mark('CSS', 12, 'marks_file.json', 'is_staff')
view.add_mark('JavaScript', 11, 'marks_file.json', 'is_staff')
view.add_mark('Python', 9, 'marks_file.json')
view.print_default_action()
view.print_courses_list()
view.print_marks_list()
view.print_courses_marks()
