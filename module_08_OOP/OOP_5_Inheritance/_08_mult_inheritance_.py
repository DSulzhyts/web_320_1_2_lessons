class A:
    def __init__(self):
        print("Class - A")


class B(A):
    def __init__(self):
        print("Class - B, from")
        super().__init__()


class C(A):
    def __init__(self):
        print("Class - C, from")
        super().__init__()


class D(C, A):
    def __init__(self):
        print("Class - D, from")
        super().__init__()


d = D()
