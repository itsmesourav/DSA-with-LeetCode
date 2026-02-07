class Solution {
    public int minimumDeletions(String s) {
        int d = 0;
        int countB = 0;

        for (char c : s.toCharArray()) {
            if (c == 'b') {
                countB++;
            } else {
                d = Math.min(d + 1, countB);
            }
        }

        return d;
    }
}
