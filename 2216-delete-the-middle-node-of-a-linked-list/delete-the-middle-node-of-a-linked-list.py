class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
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