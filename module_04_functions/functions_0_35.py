def greet_deeply_curried(greeting):
    def w_separator(separator):
        def w_emphasis(emphasis):
            def w_name(name):
                print(greeting + separator + name + emphasis)

            return w_name

        return w_emphasis

    return w_separator


greet = greet_deeply_curried("Привет")("/.../")("!")
greet("Дмитрий")
greet("Петр")

greet_deeply_curried = lambda greeting: lambda separator: lambda emphasis: lambda name: \
    print(greeting + separator + name + emphasis)

greet = greet_deeply_curried("Добрый день")("\\...\\")("?")
greet("Дмитрий")
greet("Петр")
