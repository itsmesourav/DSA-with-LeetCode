
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        price = [item[1] for item in items]
        weight = [1] * n

        # Calculate purchased + free items
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    weight[i] += 1

        ans = 0
        dp = [0] * (budget + 1)

        # Process prices from high to low
        for p in range(1500, 0, -1):
            group = [i for i in range(n) if price[i] == p]

            if not group:
                continue

            base = dp[:]
            NEG = -10**9
            has = [NEG] * (budget + 1)

            for i in group:
                cost = price[i]
                value = weight[i]

                for c in range(budget, cost - 1, -1):

                    if has[c - cost] != NEG:
                        has[c] = max(has[c], has[c - cost] + value)

                    if base[c - cost] != NEG:
                        has[c] = max(has[c], base[c - cost] + value)

                    dp[c] = max(dp[c], dp[c - cost] + value)

            # Add extra copies using the cheapest selected item
            for c in range(budget + 1):
                if has[c] != NEG:
                    total = has[c] + (budget - c) // p
                    ans = max(ans, total)

        return ans