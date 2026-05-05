# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head:
            return head
        
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next

        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]

        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            i += 1
            curr = curr.next

        return head