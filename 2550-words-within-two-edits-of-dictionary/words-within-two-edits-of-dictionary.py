class Solution(object):
    def twoEditWords(self, queries, dictionary):
        n = len(queries[0])
        res = []

        for query in queries:
            for word in dictionary:
                edits = 0
                for i in range(n):
                    if query[i] != word[i]:
                        edits += 1
                
                if edits <= 2:
                    res.append(query)
                    break
        return res