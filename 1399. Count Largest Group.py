class Solution(object):
    def countLargestGroup(self, n):
        sums = [0] * 37
        for i in range(1, n + 1):
            sums[self.digsum(i)] += 1

        maxi, count = 0, 0
        for i in sums:
            if i > maxi:
                maxi, count = i, 1
            elif i == maxi:
                count += 1
        return count

    def digsum(self, n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
