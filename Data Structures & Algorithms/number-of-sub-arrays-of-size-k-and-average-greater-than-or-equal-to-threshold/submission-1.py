class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        sum = 0
        cnt = 0
        for R in range(len(arr)):
            sum += arr[R]
            if R - L + 1 > k:
                sum -= arr[L]
                L += 1
            if R - L + 1 == k:
                avg = sum / (R - L + 1)
                if avg - threshold >= 0:
                    cnt += 1
        return cnt