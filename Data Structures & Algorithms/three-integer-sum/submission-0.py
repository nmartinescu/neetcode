class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        triplets = []
        arr.sort()
        n = len(arr)
        i = 0
        while i < n:
            L, R = i + 1, n - 1
            target = -arr[i]
            while L < R:
                if arr[L] + arr[R] == target:
                    triplets.append([arr[i], arr[L], arr[R]])
                    new_L = L
                    while new_L <= R and arr[L] == arr[new_L]:
                        new_L += 1
                    L = new_L
                elif arr[L] + arr[R] < target:
                    L += 1
                else:
                    R -= 1
            new_i = i
            while new_i < n and arr[i] == arr[new_i]:
                new_i += 1
            i = new_i
        return triplets
