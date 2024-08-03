import unittest
from module_09_datastruct.module_stack_10_1_stack.Stack_01 import Node, Stack


class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node, node_1)


class TestStack(unittest.TestCase):
    stack = Stack()

    def test_init(self):
        self.assertEqual(self.stack.top, None)

    def test_push(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.top.data, 'test_data')

    def test_pop(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.pop(), 'test_data')
        self.assertEqual(self.stack.top, None)
