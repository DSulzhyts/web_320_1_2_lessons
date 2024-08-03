def enqueue(queue, data):
    queue.append(data)


def dequeue(queue):
    if len(queue) == 0:
        return "Очередь пуста!"
    return queue.pop(0)


def peek(queue):
    if len(queue) == 0:
        return "Очередь пуста!"
    return queue[0]


def size(queue):
    return len(queue)


my_queue = []
enqueue(my_queue, 3)
enqueue(my_queue, 2)
enqueue(my_queue, 1)
print(peek(my_queue))
print(size(my_queue))
print(dequeue(my_queue))
print(dequeue(my_queue))
print(dequeue(my_queue))
print(dequeue(my_queue))
