# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.data = x
		self.next = None

class LinkedListSortWithMergeSort:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None:
            return None
        counter = 0 
        temp = head
        while temp != None:
            temp = temp.next
            counter += 1
        return self.sort(head, counter)
        
    def sort(self, head, size):
        if size == 1:
            return head
        list2 = head
        for i in range(0, size // 2):
            list2 = list2.next
        list1 = self.sort(head, size // 2)
        list2 = self.sort(list2, size - size // 2)
        return self.merge(list1, size // 2, list2, size - size // 2)
        
    def merge(self, list1, sizeList1, list2, sizeList2):
        dummy = ListNode(0)
        list = dummy
        pointer1 = 0
        pointer2 = 0
        while pointer1 < sizeList1 and pointer2 < sizeList2:
            if list1.data < list2.data:
                list.next = list1
                list1 = list1.next
                pointer1 += 1
            else:
                list.next = list2
                list2 = list2.next
                pointer2 += 1
            list = list.next
        while pointer1 < sizeList1:
            list.next = list1
            list1 = list1.next
            pointer1 += 1
            list = list.next
        while pointer2 < sizeList2:
            list.next = list2
            list2 = list2.next
            pointer2 += 1
            list = list.next
        list.next = None
        return dummy.next
