import random
import bisect

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.prefix = []
        s = 0
        for a, b, x, y in rects:
            s += (x - a + 1) * (y - b + 1)
            self.prefix.append(s)
        self.total = s

    def pick(self):
        r = random.randint(1, self.total)
        i = bisect.bisect_left(self.prefix, r)
        a, b, x, y = self.rects[i]
        width = x - a + 1
        offset = r - (self.prefix[i - 1] if i > 0 else 0) - 1
        return [a + offset % width, b + offset // width]
