class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()

        i = 0
        while i < len(costs) and coins >= costs[i]:
            coins -= costs[i]
            i += 1

        return i