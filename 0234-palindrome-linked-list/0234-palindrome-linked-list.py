# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val=[]
        while head is not None:
            val.append(head.val)
            head=head.next
        if val==val[::-1]:
            return True
        return False        