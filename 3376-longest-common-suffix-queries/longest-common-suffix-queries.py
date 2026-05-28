class TrieNode:
    def __init__(self):
        self.children =  {}
        self.smallest = inf
        self.idx = inf

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s, idx):
        curr = self.root
        if len(s) < curr.smallest:
            curr.smallest = len(s)
            curr.idx = idx

        for c in s:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

            if len(s) < curr.smallest:
                curr.smallest = len(s)
                curr.idx = idx
    
    def query(self, s):
        curr = self.root
        for c in s:
            if not c in curr.children:
                break
            curr = curr.children[c]
        return curr.idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        res = []
        for i, w in enumerate(wordsContainer):
            trie.insert(w[::-1], i)
        for w in wordsQuery:
            res.append(trie.query(w[::-1]))
        return res