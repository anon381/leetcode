
from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        even_ptr, odd_ptr = 0, 1

        for val in nums:
            if val % 2 == 0:
                result[even_ptr] = val
                even_ptr += 2
            else:
                result[odd_ptr] = val
                odd_ptr += 2

        return result
