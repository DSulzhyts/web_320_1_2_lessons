def longest_word(*args):
    print(type(args))
    leader = ""

    for word in args:
        if type(word) is str:
            if len(word) > len(leader):
                leader = word
    return leader


print(longest_word("Python", "Java", 3, [], "Программирование"))
