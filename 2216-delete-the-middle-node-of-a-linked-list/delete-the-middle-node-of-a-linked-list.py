# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        n = 0
        curr = head
        while curr:
            n = n + 1
            curr = curr.next
        
        curr = head
        curr_count = 0
        while curr:
            curr_count = curr_count + 1
            if curr_count == (n // 2):
                curr.next = curr.next.next if curr.next.next else None
                break
            curr = curr.next
        
        return head
        