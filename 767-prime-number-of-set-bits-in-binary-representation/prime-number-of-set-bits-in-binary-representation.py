class Solution(object):
    def countPrimeSetBits(self, left, right):

        """
        :type left: int
        :type right: int
        :rtype: int
        """
        primes = {2,3,5,7,11,13,17,19}
        count = 0

        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if set_bits in primes:
                count += 1
        return count
        