class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    ll_list_data = []

    def __init__(self):
        self.head = None
        self.end = None

    def insert_head(self, data):
        head_node = Node(data)
        if self.head is None:
            self.end = head_node
        else:
            head_node.next_node = self.head
        self.head = head_node

    def insert_at_end(self, data):
        node_at_end = Node(data)
        if self.head is None:
            self.head = node_at_end
        else:
            self.end.next_node = node_at_end
        self.end = node_at_end

    def print_ll(self):
        ll_string = ''
        current_node = self.head
        if current_node is None:
            print(None)
        while current_node:
            ll_string += f' {str(current_node.data)} ->'
            current_node = current_node.next_node

        ll_string += ' None'
        print(ll_string)

    def data_to_list(self):
        current_node = self.head
        while current_node.next_node is not None:
            self.ll_list_data.append(current_node.data)
            current_node = current_node.next_node
        self.ll_list_data.append(current_node.data)
        return self.ll_list_data

    def get_data_by_id(self, user_id):
        current_node = self.head
        while current_node:
            try:
                if user_id == current_node.data['id']:
                    return current_node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет 'id'!")
            current_node = current_node.next_node


ll_1 = LinkedList()
ll_1.insert_head({'id': 1, 'username': 'lazzy12345'})
ll_1.insert_at_end({'id': 2, 'username': 'mik_roz'})
ll_1.insert_at_end({'id': 3, 'username': 'mosh_s'})
ll_1.insert_head({'id': 0, 'username': 'serebro'})
ll_1.print_ll()

# lst = ll_1.data_to_list()
# for item in lst:
#     print(item)

print(ll_1.get_data_by_id(0))
ll_1.insert_at_end({'iddqd'})
ll_1.print_ll()
print(ll_1.get_data_by_id(4))
