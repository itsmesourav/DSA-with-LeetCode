class Solution:

  def sortableIntegers(self, nums: list[int]) -> int:
    n = len(nums)
    ans = 0

    # Find all divisors of n
    divisors = []
    for i in range(1, int(n**0.5) + 1):
      if n % i == 0:
        divisors.append(i)
        if i * i != n:
          divisors.append(n // i)
    divisors.sort()

    for k in divisors:
      valid = True
      prev_max = -float("inf")

      for start in range(0, n, k):
        block = nums[start : start + k]
        drops = 0
        drop_idx = -1

        for j in range(k):
          if block[j] > block[(j + 1) % k]:
            drops += 1
            drop_idx = j

        if drops > 1:
          valid = False
          break

        if drops == 0:
          min_val = block[0]
          max_val = block[-1]
        else:
          min_idx = (drop_idx + 1) % k
          max_idx = drop_idx
          min_val = block[min_idx]
          max_val = block[max_idx]

        # Ensure adjacent blocks are in non-decreasing order
        if min_val < prev_max:
          valid = False
          break

        prev_max = max_val

      if valid:
        ans += k

    return ans