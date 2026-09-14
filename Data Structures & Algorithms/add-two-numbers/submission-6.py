# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode()
        newListNode = dummyNode

        while l1 or l2 or carry:
            node1 = l1.val if l1 else 0
            node2 = l2.val if l2 else 0

            total = node1+node2+carry
            carry = total // 10

            newListNode.next = ListNode(total % 10)
            newListNode = newListNode.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummyNode.next
                
