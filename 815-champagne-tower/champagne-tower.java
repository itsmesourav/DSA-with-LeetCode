class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[] prev = new double[]{poured};
        for (int row = 1; row <= query_row; row++){
            double[] curr = new double[row + 1];

            for(int i = 0; i < prev.length; i++){
                double extra = prev[i] - 1.0;
                if(extra > 0){
                    curr[i] += extra/2.0;
                    curr[i + 1] += extra/2.0;
                }
            }

            prev = curr;
        }

        return Math.min(1.0, prev[query_glass]);
    }   
}