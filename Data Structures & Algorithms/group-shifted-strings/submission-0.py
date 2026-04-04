class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_ans = defaultdict(list)
        for string in strings:
            key = []
            for i in range(1, len(string)):
                key.append(str((ord(string[i]) - ord(string[i - 1]) + 26) % 26 + ord('a')))
            hash_ans[tuple(key)].append(string)
        return list(hash_ans.values())