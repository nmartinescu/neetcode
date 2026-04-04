class TrieNode:
    def __init__(self, c, is_word = False):
        self.c = c
        self.is_word = is_word
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode("")

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.is_word = True

    def search_trie(self, node, word):
        if word == "":
            return node.is_word
        c = word[0]
        if c not in node.children:
            if c == ".":
                for ch in node.children:
                    if self.search_trie(node.children[ch], word[1:]):
                        return True
        else:
            return self.search_trie(node.children[c], word[1:])
        return False

    def search(self, word: str) -> bool:
        return self.search_trie(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)