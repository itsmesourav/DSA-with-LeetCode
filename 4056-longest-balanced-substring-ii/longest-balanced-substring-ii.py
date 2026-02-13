class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for mask in range(1, 8):
            idx_map = {tuple([0]) * (bin(mask).count('1') - 1): -1}
            count = [0, 0, 0]

            start_indax = 0
            for i, char in enumerate(s):
                val = ord(char) - ord('a')

                if not ((mask >> val) & 1):
                    count = [0, 0, 0]

                    idx_map = {tuple([0] * (bin(mask).count('1') - 1)): i}
                    start_indax = i + 1
                    continue
                
                count[val] += 1

                state = []
                active_counts = [count[j] for j in range(3) if (mask >> j) & 1]

                if active_counts:
                    base = active_counts[0]
                    for k in range(1, len(active_counts)):
                        state.append(active_counts[k] - base)
                
                current_state = tuple(state)

                if current_state in idx_map:
                    res = max(res, i - idx_map[current_state])
                else:
                    idx_map[current_state] = i

        return res
        