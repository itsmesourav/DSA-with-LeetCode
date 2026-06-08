class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> before = new ArrayList<>();
        List<Integer> mid = new ArrayList<>();
        List<Integer> after = new ArrayList<>();

        for (int n : nums) {
            if (n < pivot) {
                before.add(n);
            } else if (n > pivot) {
                after.add(n);
            } else {
                mid.add(n);
            }
        }

        int[] result = new int[nums.length];
        int idx = 0;

        for (int n : before) result[idx++] = n;
        for (int n : mid) result[idx++] = n;
        for (int n : after) result[idx++] = n;

        return result;
    }
}