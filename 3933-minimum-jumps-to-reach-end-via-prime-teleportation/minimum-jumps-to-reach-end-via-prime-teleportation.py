from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        max_val = max(nums)

        # Smallest Prime Factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Check prime
        def is_prime(x):
            return x > 1 and spf[x] == x

        # Get unique prime factors
        def prime_factors(x):
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors

        # Map prime -> indices whose nums[i] divisible by prime
        prime_to_indices = defaultdict(list)

        for i, val in enumerate(nums):
            for p in prime_factors(val):
                prime_to_indices[p].append(i)

        q = deque([(0, 0)])  # (index, steps)
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            # Adjacent moves
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    q.append((ni, steps + 1))

            # Prime teleportation
            val = nums[i]
            if is_prime(val) and val not in used_prime:
                for ni in prime_to_indices[val]:
                    if not visited[ni]:
                        visited[ni] = True
                        q.append((ni, steps + 1))

                used_prime.add(val)

        return -1