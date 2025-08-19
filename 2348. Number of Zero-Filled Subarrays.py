
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        return (Len:=0) or sum( Len:=Len+1 if x==0 else 0 for x in nums )
## or 
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total =0
        count =0
        for n in nums:
            if n ==0:
                count=count+1
            else:
                total += count * (count + 1) // 2
                count=0
        total += count * (count + 1) // 2
        return total
