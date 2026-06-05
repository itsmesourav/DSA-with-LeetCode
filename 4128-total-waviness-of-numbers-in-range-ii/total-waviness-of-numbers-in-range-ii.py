from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def F(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, prev1, prev2):
                if pos == m:
                    return (1, 0)  # count, total_waviness

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, -1, -1)
                        total_cnt += cnt
                        total_wav += wav
                        continue

                    if not started:
                        cnt, wav = dp(pos + 1, ntight, True, d, -1)
                        total_cnt += cnt
                        total_wav += wav
                    else:
                        add = 0

                        # We already have at least two digits:
                        # prev2, prev1, d
                        if prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or \
                               (prev1 < prev2 and prev1 < d):
                                add = 1

                        cnt, wav = dp(pos + 1, ntight, True, d, prev1)

                        total_cnt += cnt
                        total_wav += wav + add * cnt

                return (total_cnt, total_wav)

            return dp(0, True, False, -1, -1)[1]

        return F(num2) - F(num1 - 1)