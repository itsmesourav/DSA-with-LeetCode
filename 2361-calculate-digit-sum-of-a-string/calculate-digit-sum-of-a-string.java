class Solution {
    public String digitSum(String s, int k) {
        while (s.length() > k) {
            StringBuilder result = new StringBuilder();

            for (int i = 0; i < s.length(); i += k) {
                String group = s.substring(i, Math.min(i + k, s.length()));

                int sum = 0;

                for (int j = 0; j < group.length(); j++) {
                    sum += group.charAt(j) - '0';
                }

                result.append(sum);
            }

            s = result.toString();
        }

        return s;
    }
}