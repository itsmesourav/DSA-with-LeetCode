class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        
        if (n == 1) {
            return true;
        }

        boolean smaller = nums[0] < nums[n - 1];

        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[i - 1]) {
                if (smaller) {
                    return false;
                }
                smaller = true;
            }
        }

        return true;
    }
}