import threading


def writer(x, event_for_wait, event_for_set):
    for i in range(10):
        event_for_wait.wait()
        event_for_wait.clear()
        print(x, end=" / ")
        event_for_set.set()


event_1 = threading.Event()
event_2 = threading.Event()

thread_1 = threading.Thread(target=writer, args=(0, event_1, event_2))
thread_2 = threading.Thread(target=writer, args=(1, event_2, event_1))

thread_1.start()
thread_2.start()

event_1.set()

thread_1.join()
thread_2.join()
