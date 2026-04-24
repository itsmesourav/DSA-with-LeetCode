class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        int l = 0, r = 0, res = 0;

    for (char m : moves.toCharArray()) {
        if (m == 'L') {
            l++;
        } else if (m == 'R') {
            r++;
        } else {
            res++;
        }
    }

    return res + Math.abs(l - r);
} }
        
    
