class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mp = {}
        pre = [0] * n
        suf = [0] * n

        for i in range(n):
            x = nums[i]
            if x in mp:
                pre[i] = mp[x][2] + (mp[x][0] * (i - mp[x][1]))
                mp[x][0] += 1
                mp[x][1] = i
                mp[x][2] = pre[i]
            else:
                mp[x] = [1, i, 0]
        
        mp = {}
        for i in range(n - 1, -1, -1):
            x = nums[i]
            if x in mp:
                suf[i] = mp[x][2] + (mp[x][0] * (mp[x][1] - i))
                mp[x][0] += 1
                mp[x][1] = i
                mp[x][2] = suf[i]
            else:
                mp[x] = [1, i, 0]
        
        res = [0] * n
        for i in range(n):
            res[i] = pre[i] + suf[i]
        return res