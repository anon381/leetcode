from collections import Counter
class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        total_counts = Counter(basket1) + Counter(basket2)
        for count in total_counts.values():
            if count % 2 != 0:
                return -1
        fruits_to_swap = []
        count1 = Counter(basket1)
        for fruit, total_count in total_counts.items():
            target = total_count // 2
            diff = count1.get(fruit, 0) - target
   
            for _ in range(abs(diff)):
                fruits_to_swap.append(fruit)
        fruits_to_swap.sort()
        min_val = min(total_counts.keys())
        total_cost = 0
        swaps_to_make = len(fruits_to_swap) // 2
        for i in range(swaps_to_make):
            total_cost += min(fruits_to_swap[i], 2 * min_val)
        return total_cost
## or 
from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        s1 = Counter(basket1)
        s2 = Counter(basket2)
        check = s1 + s2
        res = 0
        for fruit, count in check.items():
            if count % 2 != 0:
                return -1
        final = []
        excess_in_b1 = s1 - s2
        for fruit, count in excess_in_b1.items():
            final.extend([fruit] * (count // 2))
        excess_in_b2 = s2 - s1
        for fruit, count in excess_in_b2.items():
            final.extend([fruit] * (count // 2))

        final.sort()
        min_el = min(min(basket1), min(basket2))
        
        for i in range(len(final) // 2):
            swap_cost = min(2 * min_el, final[i])
            res += swap_cost
            
        return res
