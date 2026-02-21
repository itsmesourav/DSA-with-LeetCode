class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        X = sum(num.bit_count() in primes for num in range(left, right+1))
        return X
        