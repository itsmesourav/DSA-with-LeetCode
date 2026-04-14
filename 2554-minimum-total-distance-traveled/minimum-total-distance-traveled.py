class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        R = len(robot)
        factory.sort()
        F = len(factory)
        INF = 10 ** 30

        @cache
        def go(ri, fi):
            if fi == F:
                return INF
            
            best = INF
            cost = 0
            for i in range(factory[fi][1] + 1):
                if ri + i >= R:
                    best = min(best, cost)
                    break
                
                best = min(best, go(ri + i, fi + 1) + cost)
                cost += abs(factory[fi][0] - robot[ri + i])
            print(ri, fi, best)
            return best

        return go(0, 0)