class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_ad_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def insert_at_position(self, data, node_position):
        new_node = Node(data)
        if node_position == 1:
            self.insert_ad_beginning()
        """Опционально"""
        # if node_position > self.len_ll():
        #     self.insert_at_end()

        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def remove_node_index(self, rm_position):
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удалили: {removed_node.data}.\nТеперь начало {self.head.data}"

        current_node = self.head
        current_node_position = 1

        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return f"Ничего не удалили\nНачало: {self.head.data}"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f"Удалили: {removed_node.data}.\nНачало {self.head.data}"

    def remove_node_data(self, rm_data):
        if rm_data == self.head.data:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удалили: {removed_node.data}.\nТеперь начало {self.head.data}"
        current_node = self.head
        while current_node is not None and current_node.next_node is not None:
            if current_node.next_node.data == rm_data:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                return f"Удалили: {removed_node.data}.\nНачало {self.head.data}"
            else:
                return f"Ничего не удалили\nНачало: {self.head.data}"

    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def contains(self, data):
        current_node = self.head
        while current_node:
            if data == current_node.data:
                return True
            current_node = current_node.next_node
        return False

    def get(self, node_index):
        if node_index > self.len_ll():
            return "В списке нет стольких элементов"
        current_node_index = 1
        current_node = self.head
        while current_node_index <= node_index:
            if current_node_index == node_index:
                return current_node.data
            current_node_index += 1
            current_node = current_node.next_node

    def len_ll(self):
        counter = 0
        current_node = self.head
        while current_node:
            counter += 1
            current_node = current_node.next_node
        return counter


my_cats_list = LinkedList()

my_cats_list.insert_at_end('Персик_2')
my_cats_list.insert_at_end('Барсик_4')
my_cats_list.insert_at_end('Мурзик_5')
my_cats_list.insert_ad_beginning('Феликс_1')
my_cats_list.insert_at_position("Пушок_3", 3)
# print(my_cats_list.contains('Барсик_2'))
# print(my_cats_list.get(0))
# print(my_cats_list.remove_node_index(2))
# print(my_cats_list.remove_node_data('Барсик_3'))
my_cats_list.print_ll()
