# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copy_random_list(self, head):
        if None == head:
            return None
        save_list = [ ]
        p1 = head
        while None != p1:
            save_list.append(p1)
            p1 = p1.next
        new_head = RandomListNode(-1)
        new_head.next = head
        first = new_head
        second = head
        copyHead = RandomListNode(-1)
        copyFirst = copyHead
        copySecond = None
        while None != first:
            copySecond = RandomListNode(second.data) if None != second else None
            copyFirst.next = copySecond
            copyFirst = copyFirst.next
            first = first.next
            if None != second:
                second = second.next

        p1 = head
        p1_tail = head.next
        p2 = copyHead.next
        while None != p1:
            p1_tail = p1.next
            p1.next = p2
            p2.random = p1
            p1 = p1_tail
            p2 = p2.next
        p2 = copyHead.next
        while None != p2:
            p2.random = p2.random.random.next if None != p2.random.random else None
            p2 = p2.next
        len_save_list = len(save_list)
        for i in range(0, len_save_list - 1):
            save_list[i].next = save_list[i + 1]
        save_list[len_save_list - 1].next = None
        return copyHead.next
