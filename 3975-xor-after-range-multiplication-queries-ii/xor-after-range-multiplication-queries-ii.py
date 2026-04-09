class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 +  7
        n = len(nums)
        sq = int(sqrt(n))
        mp = defaultdict(list)

        for l, r, k, v in queries:
            if k > sq:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                mp[k].append((l, r, v))
        
        for k in mp:
            dif = [1] * (n + k)
            for l, r, v in mp[k]:
                dif[l] = (dif[l] * v) % MOD
                rplus1 = l + ((r - l) // k + 1) * k
                dif[rplus1] = (dif[rplus1] * pow(v, -1, MOD)) % MOD
            
            for i in range(k, n):
                dif[i] = (dif[i] * dif[i - k]) % MOD
            
            for i in range(n):
                nums[i] = (dif[i] * nums[i]) % MOD
        
        res = 0
        for x in nums:
            res ^= x
        return res