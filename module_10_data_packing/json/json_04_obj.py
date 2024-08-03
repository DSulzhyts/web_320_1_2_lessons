import json


class Figure:
    def __init__(self, title, form, color):
        self.title = title
        self.form = form
        self.color = color

    def __str__(self):
        return f"Figure: {self.title}, {repr(self.form)}, {repr(self.color)}"


class Form:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Form: {self.name}>"


class Color:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Color: {self.name}>"


class JSONDataAdapter:
    @staticmethod
    def to_json(obj):
        if isinstance(obj, Figure):
            return json.dumps({
                "title": obj.title,
                "form": obj.form.name,
                "color": obj.color.name
            })

    @staticmethod
    def from_json(obj):
        obj = json.loads(obj)

        try:
            form = Form(obj["form"])
            color = Color(obj["color"])
            figure = Figure(obj["title"], form, color)
            return figure
        except AttributeError:
            print("Неверная структура")


black = Color("Black")
yellow = Color("Yellow")
green = Color("Green")

round = Form("Rounded")
square = Form("Squared")

figure_one = Figure("Black Square", form=square, color=black)
figure_two = Figure("Yellow Circle", form=round, color=yellow)

print(figure_one)
print(figure_two)
print()

json_square = JSONDataAdapter.to_json(figure_one)
json_circle = JSONDataAdapter.to_json(figure_two)

print(json_square)
print(json_circle)
print()

square_obj = JSONDataAdapter.from_json(json_square)
circle_obj = JSONDataAdapter.from_json(json_circle)

print(square_obj)
print(circle_obj)
print(square_obj)
