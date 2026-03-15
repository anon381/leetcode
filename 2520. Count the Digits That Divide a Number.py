class Solution:
    def countDigits(self, num: int) -> int:
        return len([val for val in str(num) if num%int(val)==0])
