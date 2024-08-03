import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    # Давайте изменим список в мелком_копированном_компоненте и посмотрим, изменится ли он в компоненте в целом
    shallow_copied_component.some_list_of_objects.append("другой объект")
    if component.some_list_of_objects[-1] == "другой объект":
        print(
            "Добавление элемента в shallow_copied_component's в список "
            "some_list_of_objects добавляет это в component's some_list_of_objects (операция прошла успешно)"
        )
    else:
        print(
            "Добавление элемента в shallow_copied_component's в список "
            "some_list_of_objects НЕ добавляет это `component`'s some_list_of_objects. (операция провалилась)"
        )

    # Давайте изменим набор в списке объектов.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Изменение объектов `component`'s в some_list_of_objects "
            "изменяют этот объект в  `shallow_copied_component`'s списка "
            "some_list_of_objects. (операция прошла успешно)"
        )
    else:
        print(
            "Изменение объектов `component`'s в some_list_of_objects "
            "НЕ изменяют этот объект в `shallow_copied_component`'s списка "
            "some_list_of_objects. (операция провалилась)"
        )

    print()

    deep_copied_component = copy.deepcopy(component)
    # Давайте изменим список в deep_copied_component и посмотрим, изменится ли он в component.
    deep_copied_component.some_list_of_objects.append("еще один объект")
    if component.some_list_of_objects[-1] == "еще один объект":
        print(
            "Добавление элемента в `deep_copied_component`'s списка "
            "some_list_of_objects добавляет его к `component`'s  списка "
            "some_list_of_objects. (операция прошла успешно)"
        )
    else:
        print(
            "Добавление элемента в `deep_copied_component`'s списка "
            "some_list_of_objects НЕ добавляет его к `component`'s  списка "
            "some_list_of_objects. (операция провалилась)"
        )

    # Давайте изменим набор в списке объектов.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Изменение объектов `component`'s в some_list_of_objects "
            "изменяет этот объект в `deep_copied_component`'s списка "
            "some_list_of_objects. (операция прошла успешно)"
        )
    else:
        print(
            "Изменение объектов `component`'s в some_list_of_objects "
            "НЕ изменяет этот объект в `deep_copied_component`'s списка "
            "some_list_of_objects. (операция провалилась)"
        )

    print()

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ Это показывает, что глубоко скопированные объекты содержат одну и ту же ссылку. "
        "Они не клонируются повторно."
    )
