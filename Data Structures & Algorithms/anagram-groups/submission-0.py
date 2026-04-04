class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        sol = []
        for str in strs:
            key = [0] * 26
            for ch in str:
                key[ord(ch) - ord('a')] += 1
            value = hash_map.get(tuple(key), [])
            value.append(str)
            hash_map[tuple(key)] = value
        for key in hash_map:
            sol.append(hash_map[key])
        return sol