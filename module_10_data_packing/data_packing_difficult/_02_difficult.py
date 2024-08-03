import pickle


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node

    def print_ll_from_head(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next_node

    def print_ll_from_tail(self):
        node = self.tail
        while node is not None:
            print(node.data)
            node = node.prev_node


# box_list = LinkedList()
# box_list.insert_at_head("Барсик_1")
# box_list.insert_at_head("Снежок_0")
# box_list.insert_at_tail("Персик_2")
#
# box_list = pickle.dumps(box_list)
# print(box_list)
#
# box_list = pickle.loads(box_list)
# box_list.print_ll_from_head()
#
# with open('box_pickled.cats', 'wb') as file:
#     pickle.dump(box_list, file)
#
# with open('box_pickled.cats', 'rb') as file:
#     box_list_from_file = pickle.load(file)
#
# print(box_list_from_file)
# box_list.print_ll_from_tail()


