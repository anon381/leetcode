
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(digit) for digit in s] 
        while len(digits) > 2:
            newS = [] 
            for pos in range(0,len(digits)-1):
                pairSum = digits[pos] + (digits[pos+1] if pos+1 < len(s) else 0)
                newS.append(pairSum % 10) 
            digits = newS
        return digits[0] == digits[1]
