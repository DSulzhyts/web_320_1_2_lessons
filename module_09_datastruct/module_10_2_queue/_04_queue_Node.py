class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data


node_1 = Node(5)
node_2 = Node(3, node_1)

my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# print(my_queue.head.data)
# print(my_queue.tail.data)

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
