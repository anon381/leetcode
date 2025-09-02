class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new = sentence.split()
        count = 1 
        
        for x in range(len(new)):
            if new[x][0].casefold() in 'aeiou': 
                new[x] = new[x] + 'ma' + 'a'*count
                count += 1
            elif new[x].casefold() not in 'aeiou': 
                new[x] = new[x][1:] + new[x][0] + 'ma' + 'a'*count 
                count += 1
        
        return " ".join(x for x in new) 
