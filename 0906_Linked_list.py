# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:26:17 2019


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        dummy=ListNode(0)
        p=dummy
        while l1 is not None or l2 is not None or carry!=0:
            sum_=carry
            if l1 is not None:
                sum_+=l1.val
                l1=l1.next
            if l2 is not None:
                sum_+=l2.val
                l2=l2.next
            carry=sum_ //10
            p.next=ListNode(sum_ % 10)
            p=p.next
        return dummy.next
    