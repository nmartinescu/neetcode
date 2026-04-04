# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def quick_sort(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs    
        pivot = pairs[e]
        left = s
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
        pairs[e], pairs[left] = pairs[left], pairs[e]
        self.quick_sort(pairs, s, left - 1)
        self.quick_sort(pairs, left + 1, e)
        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quick_sort(pairs, 0, len(pairs) - 1)