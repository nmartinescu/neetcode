class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for detail in details:
            if int(detail[-4]) * 10 + int(detail[-3]) >= 60:
                ans += 1
        return ans