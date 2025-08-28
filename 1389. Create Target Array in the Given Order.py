class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        #With insert
        arr=[]
        for n,i in zip(nums,index): 
            arr.insert(i,n)
        return arr

        
        #With out insert
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for n,i in zip(nums,index): 
            arr[i:i] = [n]
        return arr
