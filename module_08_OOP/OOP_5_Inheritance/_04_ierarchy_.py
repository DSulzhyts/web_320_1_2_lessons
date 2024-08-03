class One:
    def do_it(self):
        print("doit from One")

    def do_anything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("doit from Two")


one = One()
two = Two()
one.do_anything()
two.do_anything()
