import threading


def print_numbers():
    for i in range(10):
        print(i, end=" ")


thread_1 = threading.Thread(target=print_numbers)
thread_2 = threading.Thread(target=print_numbers)
thread_1.start()
thread_2.start()
