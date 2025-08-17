from typing import List
from collections import defaultdict
def helper(s, word_map, memo):
    if s in memo:
        return memo[s]
    
    sentences = []
    if word_map[s] == 1:
        sentences = [s]
    
    for i in range(1, len(s)):
        prefix = s[:i]
        if word_map[prefix] == 1:
            suffix_sentences = helper(s[i:], word_map, memo)
            for sentence in suffix_sentences:
                sentences.append(prefix + " " + sentence)
    
    memo[s] = sentences
    return sentences

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_map = defaultdict(lambda: 0)
        for word in wordDict:
            word_map[word] = 1
        
        return helper(s, word_map, {})
