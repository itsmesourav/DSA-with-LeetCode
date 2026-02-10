class Solution {
    public int longestBalanced(int[] nums) {
        int maxLen = 0;
        int n = nums.length;
        for(int i = 0; i < n; i++) {
            Set<Integer> odd = new HashSet<>();
            Set<Integer> even = new HashSet<>();

            for(int j = i; j < n; j++) {
                if(nums[j] % 2 != 0) {
                    odd.add(nums[j]);
                } else {
                    even.add(nums[j]);
                }
                if (odd.size() == even.size()) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
}