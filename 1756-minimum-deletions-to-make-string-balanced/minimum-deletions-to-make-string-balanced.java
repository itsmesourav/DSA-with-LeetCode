class Solution {
    public int minimumDeletions(String s) {
        int d = 0;
        int countB = 0;

        for (int c=0;c<s.length();c++) {
            if (s.charAt(c) == 'b') {
                countB++;
            } else {
                d = Math.min(d + 1, countB);
            }
        }

        return d;
    }
}
