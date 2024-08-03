class Queue:
    def __init__(self, queue: list = None):
        if queue is None:
            self.__queue = []
        else:
            self.__queue = queue

    def enqueue(self, data):
        self.__queue.append(data)

    def dequeue(self):
        if len(self.__queue) == 0:
            return "Очередь пуста!"
        return self.__queue.pop(0)

    def peek(self):
        if len(self.__queue) == 0:
            return "Очередь пуста!"
        return self.__queue[0]

    def size(self):
        return len(self.__queue)


my_queue = Queue()
my_queue.enqueue(3)
my_queue.enqueue(2)
my_queue.enqueue(1)

# print(my_queue.peek())
# print(my_queue.size())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
