class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        sum_list = []
        sumation = 0
        for i in range(n):
            sumation = i+sumation+1
            sum_list.append(sumation)
        sum_last = 0
        for i in range(n):
            x = 1 -i
            sum_last+=n-i
            if (sum_last in sum_list[:x]) and (sum_list.index(sum_last) == n-i -1):
                return n-i
        return -1
           

            
