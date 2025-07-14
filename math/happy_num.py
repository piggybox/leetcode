class Solution:
    def isHappy(self, n: int) -> bool:
        # the key is to check if there's a cycle in the sequence of sums
        # if we reach 1, it's a happy number; if we see a number again, it's not
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1