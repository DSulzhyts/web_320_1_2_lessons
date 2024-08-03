class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_teacher_name(self):
        return self.__name

    def get_teacher_education(self):
        return self.__education

    def get_teacher_experience(self):
        return self.__experience

    def set_teacher_experience(self, experience):
        self.__experience = experience

    def get_teacher_data(self):
        print(f"{self.__name}, образование {self.__education}, опыт работы {self.__experience}.")

    def add_mark(self, student_name, mark):
        print(f"{self.__name} поставил оценку {mark} студенту {student_name}.")

    def remove_mark(self, student_name, mark):
        print(f"{self.__name} удалил оценку {mark} студенту {student_name}.")

    def give_a_consultation(self, student_class):
        print(f"{self.__name} провел консультацию в классе {student_class}.")


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        super().get_teacher_data()
        print(f"Предмет {self.__discipline}, должность {self.__job_title}")

    def add_mark(self, student_name, mark):
        super().add_mark(student_name, mark)
        print(f"Предмет {self.__discipline}")

    def remove_mark(self, student_name, mark):
        super().remove_mark(student_name, mark)
        print(f"Предмет {self.__discipline}")

    def give_a_consultation(self, student_class):
        super().give_a_consultation(student_class)
        print(f"По предмету {self.__discipline}, как {self.__job_title}")


chemistry_teacher = DisciplineTeacher("Иван Петров", "БГПУ", "4 года",
                                      "Химия", "Завуч")
print(chemistry_teacher.get_discipline())
print(chemistry_teacher.get_job_title())
chemistry_teacher.set_job_title("Директор")
print(chemistry_teacher.get_job_title())
chemistry_teacher.get_teacher_data()
chemistry_teacher.add_mark("Николай Иванов", 4)
chemistry_teacher.remove_mark("Дмитрий Сидоров", 3)
chemistry_teacher.give_a_consultation("10 Б")
