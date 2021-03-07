class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0

        rev_x = int(str(abs(x))[::-1])
        if negative:
            rev_x *= -1

        if -2147483649 < rev_x < 2147483648:
            return rev_x
        return 0