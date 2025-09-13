
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for x in range(lowLimit, highLimit + 1):
            count = 0
            while x:
                count += x % 10
                x //= 10
            d[count] += 1

        return max(d.values())


#in cpp
