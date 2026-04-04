class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        
        arr = self.hash_map[key]
        l, r = 0, len(arr) - 1
        ans = None
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][1] == timestamp:
                ans = arr[m][0]
                break
            elif arr[m][1] < timestamp:
                ans = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans if ans else ""

