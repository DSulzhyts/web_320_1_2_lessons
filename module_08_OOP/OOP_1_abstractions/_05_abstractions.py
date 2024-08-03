class Question:
    def __init__(self, question, answer):
        self.__question = question
        self.__answer = answer
        # self.question = question
        # self.answer = answer

    def get_question(self):
        return self.__question

    def get_answer(self):
        return self.__answer

    def check(self, answer):
        return answer == self.__answer

    @staticmethod
    def get_data(filename):
        questions_list = []
        with open(filename, 'rt', encoding='utf-8') as file:
            lines_list = file.readlines()
            for line in lines_list:
                line_list = line.strip().split('::')
                questions_list.append(line_list)
        return questions_list


question_1 = Question("My name __ Vova", "is")

questions_data = Question.get_data('questions.txt')

questions_objects = []
for question in questions_data:
    questions_objects.append(Question(question[0], question[1]))

for question in questions_objects:
    question.a = "to"
    print(question.get_question())
    user_answer = input("Введите ответ: ")
    if question.check(user_answer):
        print("Ответ верный!")
    else:
        print("Ответ неверный")
        print(f"Правильный ответ {question.get_answer()}")
