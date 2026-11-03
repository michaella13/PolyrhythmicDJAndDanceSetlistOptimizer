#!/usr/bin/env python3

import unittest
from doubly_linked_list import DoublyLinkedList

class DoublyLinkedListTest(unittest.TestCase):
    AssignmentTotal = 35
    Total  = 6
    Points = 0

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        assignment_points = cls.AssignmentTotal * cls.Points / cls.Total
        print()
        print(f'   Score {assignment_points:.2f} / {cls.AssignmentTotal:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_insert_after(self):
        dll = DoublyLinkedList()       
        dll._insert_after(dll.head, 1)
        dll._insert_after(dll.head.next, 3)
        dll._insert_after(dll.head.next, 2)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.head.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.data, 3)

    def test_pop_node(self):
        dll = DoublyLinkedList()
        dll._insert_after(dll.head, 3)
        dll._insert_after(dll.head, 2)
        dll._insert_after(dll.head, 1)
        self.assertEqual(dll._pop_node(dll.head.next.next), 2)
        self.assertEqual(dll._pop_node(dll.tail.prev), 3)
        self.assertEqual(dll._pop_node(dll.head.next), 1)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.size, 0)
            
    def test_append(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.head.next.next.data, 2)
        self.assertEqual(dll.tail.prev.data, 2)
        self.assertEqual(dll.size, 2)

    def test_insert(self):
        dll = DoublyLinkedList()
        dll.append(3)
        dll.append(5)
        dll.insert(1, 4)
        self.assertEqual(dll.head.next.data, 3)
        self.assertEqual(dll.head.next.next.data, 4)
        self.assertEqual(dll.head.next.next.next.data, 5)
        self.assertEqual(dll.tail.prev.data, 5)
        self.assertEqual(dll.size, 3)
        dll.insert(0, 1)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.head.next.next.data, 3)
        self.assertEqual(dll.head.next.next.next.data, 4)
        self.assertEqual(dll.head.next.next.next.next.data, 5)
        self.assertEqual(dll.tail.prev.data, 5)
        self.assertEqual(dll.size, 4)
        dll.insert(-3, 2)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.head.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.data, 3)
        self.assertEqual(dll.head.next.next.next.next.data, 4)
        self.assertEqual(dll.head.next.next.next.next.next.data, 5)
        self.assertEqual(dll.tail.prev.data, 5)
        self.assertEqual(dll.size, 5)
        dll.insert(-5, 0)
        self.assertEqual(dll.head.next.data, 0)
        self.assertEqual(dll.head.next.next.data, 1)
        self.assertEqual(dll.head.next.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.next.data, 3)
        self.assertEqual(dll.head.next.next.next.next.next.data, 4)
        self.assertEqual(dll.head.next.next.next.next.next.next.data, 5)
        self.assertEqual(dll.tail.prev.data, 5)
        self.assertEqual(dll.size, 6)
        dll.append(7)
        dll.insert(-1, 6)
        self.assertEqual(dll.head.next.data, 0)
        self.assertEqual(dll.head.next.next.data, 1)
        self.assertEqual(dll.head.next.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.next.data, 3)
        self.assertEqual(dll.head.next.next.next.next.next.data, 4)
        self.assertEqual(dll.head.next.next.next.next.next.next.data, 5)
        self.assertEqual(dll.head.next.next.next.next.next.next.next.data, 6)
        self.assertEqual(dll.head.next.next.next.next.next.next.next.next.data, 7)
        self.assertEqual(dll.tail.prev.data, 7)
        self.assertEqual(dll.size, 8)
        dll.insert(8, 8)
        self.assertEqual(dll.tail.prev.data, 8)
        self.assertEqual(dll.size, 9)
        with self.assertRaises(IndexError):
            dll.insert(10, 10)
        with self.assertRaises(IndexError):
            dll.insert(-10, 10)
        dll = DoublyLinkedList()
        dll.insert(0, 1)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.tail.prev.data, 1)
        self.assertEqual(dll.size, 1)

    def test_clear(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.clear()
        self.assertEqual(dll.size, 0)
        self.assertEqual(dll.head.next, dll.tail)
        self.assertEqual(dll.tail.prev, dll.head)

    def test_index(self):
        dll = DoublyLinkedList()
        for i in range(5):
            dll.append(i)
        self.assertEqual(dll.index(0), 0)
        self.assertEqual(dll.index(3), 3)
        self.assertEqual(dll.index(4), 4)
        self.assertEqual(dll.index(5), -1)

    def test_bool(self):
        dll = DoublyLinkedList()
        if dll:
            self.fail()
        dll.append(1)
        if not dll:
            self.fail()

    def test_contains(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        self.assertTrue(1 in dll)
        self.assertTrue(2 in dll)
        self.assertFalse(3 in dll)

    def test_len(self):
        dll = DoublyLinkedList()
        self.assertEqual(len(dll), 0)
        dll.append(1)
        self.assertEqual(len(dll), 1)
        dll.append(2)
        self.assertEqual(len(dll), 2)
        dll.pop(0)
        self.assertEqual(len(dll), 1)
        dll.pop(0)
        self.assertEqual(len(dll), 0)

    def test_iter(self):
        dll = DoublyLinkedList()
        self.assertEqual(list(dll), [])
        for i in [1, 2, 3]:
            dll.append(i)
        lst = []
        for i in dll:
            lst.append(i)
        self.assertEqual(lst, [1, 2, 3])

    def test_iter_nested(self):
        dll = DoublyLinkedList()
        for i in [1, 2, 3]:
            dll.append(i)
        pairs = [(a, b) for a in dll for b in dll]
        self.assertEqual(len(pairs), 9)
        self.assertEqual(pairs[:3], [(1, 1), (1, 2), (1, 3)])
        self.assertEqual(list(zip(dll, dll)), [(1, 1), (2, 2), (3, 3)])
        lst = []
        for i in dll:
            str(dll)
            lst.append(i)
        self.assertEqual(lst, [1, 2, 3])

    def test_str(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        self.assertEqual(str(dll), "1 2 3")

    #---- Homework Method Tests ----#

    def test_get_node(self):
        dll = DoublyLinkedList()
        with self.assertRaises(IndexError):
            dll._get_node(0)
        with self.assertRaises(IndexError):
            dll._get_node(-1)
        for i in range(5):
            dll.append(i)
        self.assertIs(dll._get_node(0), dll.head.next)
        self.assertIs(dll._get_node(-1), dll.tail.prev)
        self.assertEqual(dll._get_node(2).data, 2)
        self.assertEqual(dll._get_node(4).data, 4)
        self.assertEqual(dll._get_node(-2).data, 3)
        self.assertEqual(dll._get_node(-5).data, 0)
        with self.assertRaises(IndexError):
            dll._get_node(5)
        with self.assertRaises(IndexError):
            dll._get_node(-6)
        DoublyLinkedListTest.Points += 1

    def test_insert_ordered(self):
        dll = DoublyLinkedList()
        dll.insert_ordered(3)
        dll.insert_ordered(1)
        dll.insert_ordered(2)
        dll.insert_ordered(4)
        dll.insert_ordered(0)
        self.assertEqual(dll.size, 5)
        self.assertEqual(dll.head.next.data, 0)
        self.assertEqual(dll.head.next.next.data, 1)
        self.assertEqual(dll.head.next.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.next.data, 3)
        self.assertEqual(dll.head.next.next.next.next.next.data, 4)
        self.assertEqual(dll.tail.prev.data, 4)
        DoublyLinkedListTest.Points += 1

    def test_pop(self):
        dll = DoublyLinkedList()
        for i in range(5):
            dll.append(i)
        self.assertEqual(dll.pop(2), 2)
        self.assertEqual(dll.pop(0), 0)
        self.assertEqual(dll.pop(-1), 4)
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.head.next.next.data, 3)
        self.assertEqual(dll.tail.prev.data, 3)
        with self.assertRaises(IndexError):
            dll.pop(2)
        with self.assertRaises(IndexError):
            dll.pop(-3)
        DoublyLinkedListTest.Points += 1

    def test_sort(self):
        dll = DoublyLinkedList()
        dll.append(3)
        dll.append(1)
        dll.append(2)
        dll.append(4)
        dll.append(0)
        dll.sort()
        self.assertEqual(dll.head.next.data, 0)
        self.assertEqual(dll.head.next.next.data, 1)
        self.assertEqual(dll.head.next.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.next.data, 3)
        self.assertEqual(dll.head.next.next.next.next.next.data, 4)
        self.assertEqual(dll.tail.prev.data, 4)
        self.assertEqual(dll.size, 5)
        DoublyLinkedListTest.Points += 1

    def test_getitem(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(11)
        self.assertEqual(dll[0], 10)
        self.assertEqual(dll[1], 11)
        self.assertEqual(dll[-2], 10)
        self.assertEqual(dll[-1], 11)
        with self.assertRaises(IndexError):
            dll[2]
        with self.assertRaises(IndexError):
            dll[-3]
        DoublyLinkedListTest.Points += 1

    def test_setitem(self):
        dll = DoublyLinkedList()
        dll.append(10)
        dll.append(11)
        dll[0] = 20
        self.assertEqual(dll[0], 20)
        dll[1] = 21
        self.assertEqual(dll[1], 21)
        dll[-2] = 30
        self.assertEqual(dll[0], 30)
        dll[-1] = 31
        self.assertEqual(dll[1], 31)
        with self.assertRaises(IndexError):
            dll[2] = 4
        DoublyLinkedListTest.Points += 1

if __name__ == '__main__':
    unittest.main()