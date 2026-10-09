# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pr,c= None,head

        while c:
            temp=c.next
            c.next=pr
            pr=c
            c=temp
        return pr
