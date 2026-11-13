from collections import deque


class Solution(object):

  def countNonDecreasingSubarrays(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ans = 0
    cost = 0
    dq = deque()
    j = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
      num = nums[i]
      while dq and nums[dq[-1]] < num:
        l = dq.pop()
        r = dq[-1] if dq else j + 1
        cost += (r - l) * (num - nums[l])
      dq.append(i)

      while cost > k:
        cost -= nums[dq[0]] - nums[j]
        if dq[0] == j:
          dq.popleft()
        j -= 1

      ans += j - i + 1

    return ans