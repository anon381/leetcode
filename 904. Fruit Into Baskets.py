from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = 0
        max_len = 0
        fruit_count = defaultdict(int)

        for end in range(len(fruits)):
            fruit_count[fruits[end]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
## or another approach 
from collections import defaultdict

class Solution:
def totalFruit(fruits):
    last = second_last = -1
    last_count = curr = res = 0

    for f in fruits:
        if f == last or f == second_last:
            curr += 1
        else:
            curr = last_count + 1

        if f == last:
            last_count += 1
        else:
            last_count = 1
            second_last, last = last, f

        res = max(res, curr)

    return res
