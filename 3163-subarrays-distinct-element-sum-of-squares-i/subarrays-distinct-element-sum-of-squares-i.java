import java.util.*;

class Solution {
    public int sumCounts(List<Integer> nums) {
        int total = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            Set<Integer> seen = new HashSet<>();

            for (int j = i; j < n; j++) {
                seen.add(nums.get(j));
                int count = seen.size();
                total += count * count;
            }
        }

        return total;
    }
}