class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        n = len(arr)
        crit = []
        for i in range(1, n - 1):
            if arr[i - 1] > arr[i] < arr[i + 1] or arr[i - 1] < arr[i] > arr[i + 1]:
                crit.append(i)

        if len(crit) < 2:
            return [-1, -1]

        mx = crit[-1] - crit[0]
        mn = inf
        for i in range(1, len(crit)):
            mn = min(mn, crit[i] - crit[i - 1])
        return [mn, mx]