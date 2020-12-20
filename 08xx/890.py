class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def word_matches(word, pattern):
            permutations = dict()
            for i in range(len(word)):
                if pattern[i] in permutations:
                    if permutations[pattern[i]] != word[i]:
                        return False
                else:
                    permutations[pattern[i]] = word[i]
            return len(set(permutations.values())) == len(set(permutations.keys()))
        
        result = []
        for word in words:
            if word_matches(word, pattern):
                result.append(word)
        return result
