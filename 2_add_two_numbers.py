# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        if l1 is not None and l2 is not None:
            i = l1.val + l2.val
            if l1.next is not None and l2.next is not None:
                l1_next = l1.next
                l2_next = l2.next
                l1_next.val += i//10
                return (ListNode(i%10,self.addTwoNumbers(l1_next,l2_next)))
            elif l1.next is not None:
                l1_next = l1.next
                l1_next.val += i//10
                return (ListNode(i%10,self.addTwoNumbers(l1_next,None)))
            elif l2.next is not None :
                l2_next = l2.next
                l2_next.val += i//10
                return (ListNode(i%10,self.addTwoNumbers(l2_next,None)))
            elif i//10 > 0:
                return (ListNode(i%10,self.addTwoNumbers(None,None)))
            else :
                return (ListNode(i))
        elif l1 is not None:
            i = l1.val
            if l1.next is not None:
                l1_next = l1.next
                l1_next.val += i//10
                return (ListNode(i%10,self.addTwoNumbers(l1_next,None)))
            elif i//10 > 0:
                return (ListNode(i%10,self.addTwoNumbers(None,None)))
            else :
                return (ListNode(i))
        elif l2 is not None:
            i = l2.val
            if l2.next is not None:
                l2_next = l2.next
                l2_next.val += i//10
                return (ListNode(i%10,self.addTwoNumbers(l2_next,None)))
            elif i//10 > 0:
                return (ListNode(i%10,self.addTwoNumbers(None,None)))
            else :
                return (ListNode(i))
        else :
            return (ListNode(1))
        