from threading import Thread, Lock
from time import sleep

counter = 0


def increase(by, lock):
    global counter
    lock.acquire()
    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f"Значение counter: {counter}")

    lock.release()


my_lock = Lock()

thread_1 = Thread(target=increase, args=(10, my_lock))
thread_2 = Thread(target=increase, args=(20, my_lock))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f'Значение counter в итоге: {counter}')
