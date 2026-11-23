import java.util.ArrayList;
import java.util.List;

class ProductOfNumbers {

    List<Integer> prefix;

    public ProductOfNumbers() {
        prefix = new ArrayList<>();
        prefix.add(1);
    }
    
    public void add(int num) {
        if (num == 0) {
            prefix.clear();
            prefix.add(1);
        } else {
            int last = prefix.get(prefix.size() - 1);
            prefix.add(last * num);
        }
    }
    
    public int getProduct(int k) {
        if (k >= prefix.size()) {
            return 0;
        }

        int n = prefix.size();
        return prefix.get(n - 1) / prefix.get(n - k - 1);
    }
}