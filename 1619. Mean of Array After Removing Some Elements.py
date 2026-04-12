import math
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        x = math.ceil(len(arr)/20)
        for i in range(x):
            arr.pop()
          
        arr.sort(reverse = True)
        for i in range(x):
            print(arr[i])
            arr.pop()
        sum = 0
        for i in arr:
            sum+=i
        return sum/len(arr)
