class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        hash_map = collections.defaultdict(set)

        if len(sentence1) != len(sentence2):
            return False

        for pair in similarPairs:
            word1, word2 = pair[0], pair[1]
            hash_map[word1].add(word2)
            hash_map[word2].add(word1)
        
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word2 not in hash_map[word1] and word1 != word2:
                return False
        return True