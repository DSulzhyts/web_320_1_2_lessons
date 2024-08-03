class Component:

    def operation(self):
        pass


class ConcreteComponent(Component):

    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):

    def operation(self):
        return f'ConcreteDecoratorA ({self.component.operation()})'


class ConcreteDecoratorB(Decorator):

    def operation(self):
        return f'ConcreteDecoratorB ({self.component.operation()})'


def client_code(component: Component):
    print(f"Result: {component.operation()}", end="")


simple = ConcreteComponent()
print("Client: У меня простой компонент:")
client_code(simple)
print("\n")

decorator1 = ConcreteDecoratorA(simple)
print("Client: Теперь у меня декорированный компонент:")
client_code(decorator1)
print("\n")

decorator2 = ConcreteDecoratorB(decorator1)
print("Client: Теперь я декорировал, декорированный компонент:")
client_code(decorator2)
