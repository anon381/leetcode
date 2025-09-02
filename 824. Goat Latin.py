class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new = sentence.split() # Breaks up the input into individual sentences
        count = 1 # Starting at 1 since we only have one "a" to begin with.
        
        for x in range(len(new)):
            if new[x][0].casefold() in 'aeiou': # Checks if the first value of x is a vowel. The casefold, can be replaced with lower, lowers the case. Can also just be removed and have "in 'aeiouAEIOU'
                new[x] = new[x] + 'ma' + 'a'*count # Brings it together with the count multiplying number of "a"'s as needed.
                count += 1
            elif new[x].casefold() not in 'aeiou': # Same comment as above.
                new[x] = new[x][1:] + new[x][0] + 'ma' + 'a'*count # Just moves the first value to the end then does the a.
                count += 1
        
        return " ".join(x for x in new) # Converts the list back into a string.
