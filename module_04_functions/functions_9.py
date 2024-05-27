def remove_from_string(string, *args):
    for symbol in args:
        string = string.replace(symbol, "")

    return string


print(remove_from_string("Смотри! Мы, можем удалить: все знаки препинания сразу. Или нет?", "?", ".", ",", "!", ":"))
