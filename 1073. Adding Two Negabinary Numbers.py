from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []  

        while i >= 0 or j >= 0 or carry != 0:
            a = arr1[i] if i >= 0 else 0
            b = arr2[j] if j >= 0 else 0
            total = a + b + carry

            if total >= 2:
                res.append(total - 2)  
                carry = -1
            elif total >= 0:
                res.append(total)      
                carry = 0
            else:  
                res.append(1)
                carry = 1

            i -= 1
            j -= 1

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return res[::-1]

