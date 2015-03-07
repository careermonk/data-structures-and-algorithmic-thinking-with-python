import random
import unittest
from DLL import DoubleLinkedList

class TestSequenceFunctions(unittest.TestCase):


    def test_insert(self):
        dll = DoubleLinkedList()
        dll.insert("alice")
        self.assertEqual(dll.getNode(0).getData(), "alice")

        dll.insert("bob")
        dll.insert("charlie")
        self.assertEqual(dll.getNode(1).getData(), "bob")
        self.assertEqual(dll.getNode(2).getData(), "charlie")

        # insert a node after bill, fixes insertAtGivenPosition logic
        # bill should go in between bob and charlie
        dll.insertAtGivenPosition(1, "bill")
        self.assertEqual(dll.getNode(2).getData(), "bill")
        self.assertEqual(dll.getNode(2).getPrev().getData(), "bob")
        self.assertEqual(dll.getNode(2).getNext().getData(), "charlie")

        #insert an index that should go on the end and exercise the 
        # insertAtEnd method which didn't exist
        dll.insertAtGivenPosition(100, "donna")
        self.assertEqual(dll.getNode(4).getData(), "donna")

    def test_delete(self):
        dll = DoubleLinkedList()
        dll.insert("alice")
        dll.insert("bob")
        dll.insert("charlie")
        self.assertEqual(dll.getNode(2).getData(), "charlie")

        # charlie should shift over now to where bob was
        dll.delete("bob")
        self.assertEqual(dll.getNode(1).getData(), "charlie")



if __name__ == '__main__':
    unittest.main()


