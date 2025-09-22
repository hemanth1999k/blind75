class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        curr = head
        while(curr.next!=None):
            val = curr.next.val
            curr.next.val = curr.val
            curr.val = val

            if(curr.next.next!= None):
                curr = curr.next.next
            else:
                break
        return head
        