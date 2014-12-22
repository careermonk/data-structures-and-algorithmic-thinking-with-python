# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves
# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.next = None
         # method for setting the data field of the node    
    def setData(self, data):
        self.data = data
    # method for getting the data field of the node   
    def getData(self):
        return self.data
      # method for setting the next field of the node
    def setNext(self, next):
        self.next = next
       # method for getting the next field of the node    
    def getNext(self):
        return self.next
    # returns true if the node points to another node
    def hasNext(self):
            return self.next != None
	    
def _splitList(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.getNext()
        fast = fast.getNext()
        fast = fast.getNext()

    middle = slow.getNext()
    slow.setNext(None)

    return head, middle

# Reverses in place a list.
# @return Returns the head of the new reversed list
def _reverseList(head):

  last = None
  currentNode = head

  while currentNode:
    nextNode = currentNode.getNext()
    currentNode.setNext(last)
    last = currentNode
    currentNode = nextNode

  return last

# Merges in place two lists
def _mergeLists(a, b):
    tail = a
    head = a
    a = a.getNext()
    while b:
        tail.setNext(b)
        tail = tail.getNext()
        b = b.getNext()
        if a:
            a, b = b, a
    return head

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)
