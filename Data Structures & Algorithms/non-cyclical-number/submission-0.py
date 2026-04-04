class Solution:
    def sum_of_digit_squares(self, number):
        ans = 0
        while number:
            digit = number % 10
            ans += digit ** 2
            number //= 10
        return ans

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum_of_digit_squares(n)

        while slow != 1 and slow != fast:
            slow = self.sum_of_digit_squares(slow)
            fast = self.sum_of_digit_squares(self.sum_of_digit_squares(fast))
        return slow == 1
