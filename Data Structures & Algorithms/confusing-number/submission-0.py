class Solution:
    def confusingNumber(self, n: int) -> bool:
        aux = n
        reversed = 0
        while aux:
            digit = aux % 10
            if digit in (2, 3, 4, 5, 7):
                return False
            if digit == 6:
                digit = 9
            elif digit == 9:
                digit = 6
            reversed = reversed * 10 + digit
            aux //= 10
        return True if reversed != n else False