class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        heap = []
        ans = []
        n = len(nums)

        for i in range(k):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
                heapq.heappush(heap, -nums[i])
        ans.append(-heap[0])
        for i in range(k, n):
            to_delete = nums[i - k]    
            hash_map[to_delete] -= 1
            
            to_add = nums[i]
            val = hash_map.get(to_add, 0)
            if not val:
                heapq.heappush(heap, -to_add)
            hash_map[to_add] = val + 1
            while heap and hash_map[-heap[0]] == 0:
                heapq.heappop(heap)
            ans.append(-heap[0])
        return ans