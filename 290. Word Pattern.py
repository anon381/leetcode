class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        seen = {}

        for p, w in zip(pattern, words):
            key_p = ("p", p)
            key_w = ("w", w)

            if key_p in seen and seen[key_p] != w:
                return False
            if key_w in seen and seen[key_w] != p:
                return False
            
            seen[key_p] = w
            seen[key_w] = p
        
        return True
