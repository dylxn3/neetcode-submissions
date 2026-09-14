# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head

        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        
        secondlist = l1.next
        l1.next = None
        previous = None

        while secondlist:
            tmp = secondlist.next
            secondlist.next = previous 
            previous = secondlist
            secondlist = tmp


        first = head
        second = previous

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
