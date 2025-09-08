# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        curr = head
        l=1
        while curr.next:
            l+=1
            curr=curr.next
        le= l- (k%l)
        curr.next=head
        if le==0:
            return head
        nhead=head
        tail = None
        while le:
            tail=nhead
            nhead=nhead.next
            le-=1
        tail.next=None

        return nhead
        