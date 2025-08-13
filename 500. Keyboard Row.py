class Solution:
    def findWords(self, words: List[str]) -> List[str]: 
        res = []
        top = set("qwertyuiop")
        mid = set("asdfghjkl")
        bot = set("zxcvbnm")
        
        for word in words: 
            wordset = set(word.lower())
            if wordset <= top or wordset <= mid or wordset <= bot: 
                res.append(word)
        return res 
