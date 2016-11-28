#!python

from linked_list import Linked_List, Node
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        assert node.data is data
        assert node.next is None


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        ll = Linked_List()
        assert ll.head is None
        assert ll.tail is None

    def test_init_with_list(self):
        ll = Linked_List(['A', 'B', 'C'])
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'

    def test_as_list(self):
        ll = Linked_List()
        assert ll.as_list() == []
        ll.append('A')
        assert ll.as_list() == ['A']
        ll.append('B')
        assert ll.as_list() == ['A', 'B']
        ll.append('C')
        assert ll.as_list() == ['A', 'B', 'C']

    def test_length(self):
        ll = Linked_List()
        assert ll.length() == 0
        ll.append('A')
        assert ll.length() == 1
        ll.append('B')
        assert ll.length() == 2
        ll.append('C')
        assert ll.length() == 3

    def test_append(self):
        ll = Linked_List()
        ll.append('A')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'A'
        ll.append('B')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'B'
        ll.append('C')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'

    def test_prepend(self):
        ll = Linked_List()
        ll.prepend('C')
        assert ll.head.data == 'C'
        assert ll.tail.data == 'C'
        ll.prepend('B')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        ll.prepend('A')
        assert ll.head.data == 'A'
        assert ll.tail.data == 'C'

    def test_delete(self):
        ll = Linked_List()
        ll.append('A')
        ll.append('B')
        ll.append('C')
        print(ll.as_list())
        ll.delete('A')
        print(ll.as_list())
        assert ll.head.data == 'B'
        assert ll.tail.data == 'C'
        ll.delete('C')
        assert ll.head.data == 'B'
        assert ll.tail.data == 'B'
        ll.delete('B')
        assert ll.head is None
        assert ll.tail is None
        with self.assertRaises(ValueError):
            ll.delete('D')

    def test_find(self):
        ll = Linked_List()
        ll.append('A')
        ll.append('B')
        ll.append('C')
        assert ll.find(lambda item: item == 'B') == 'B'
        assert ll.find(lambda item: item < 'B') == 'A'
        assert ll.find(lambda item: item > 'B') == 'C'
        assert ll.find(lambda item: item == 'D') is None


if __name__ == '__main__':
    unittest.main()
