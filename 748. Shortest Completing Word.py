class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words=sorted(words, key=len)
        plate=Counter(i.lower() for i in licensePlate if i.isalpha())

        for i in words:
            if Counter(i)>=plate:
                return i

  ## or 

class Solution:
    def shortestCompletingWord(self, license_plate: str, words: List[str]) -> str:
        letters = Counter(ltr.lower() for ltr in license_plate if ltr.isalpha())
        return min((word for word in words if not letters - Counter(word)), key=len)
