from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)])
        
        stack = []  # stores indices in 'robots' list
        
        # Convert to list for mutability
        healths = list(healths)
        
        for i in range(n):
            pos, h, d, idx = robots[i]
            
            if d == 'R':
                stack.append(i)
            else:  # d == 'L'
                while stack and healths[idx] > 0:
                    j = stack[-1]
                    _, _, _, prev_idx = robots[j]
                    
                    if healths[prev_idx] < healths[idx]:
                        # R robot dies
                        stack.pop()
                        healths[idx] -= 1
                        healths[prev_idx] = 0
                    elif healths[prev_idx] > healths[idx]:
                        # L robot dies
                        healths[prev_idx] -= 1
                        healths[idx] = 0
                        break
                    else:
                        # both die
                        stack.pop()
                        healths[prev_idx] = 0
                        healths[idx] = 0
                        break
        
        # Collect survivors in original order
        result = []
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])
        
        return result