
class Solution:
    def build(self, ind, low, high, target):
        if low == high:
            self.seg[ind] = (target[low], low) 
            return
        mid = (low + high) // 2
        self.build(2 * ind + 1, low, mid, target)
        self.build(2 * ind + 2, mid + 1, high, target)
        self.seg[ind] = min(self.seg[2 * ind + 1], self.seg[2 * ind + 2])

    def query(self, ind, low, high, l, r):
        if high < l or low > r:  
            return (sys.maxsize, sys.maxsize)
        if l <= low and high <= r:  
            return self.seg[ind]

        mid = (low + high) // 2  # Partial overlap
        left = self.query(2 * ind + 1, low, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return min(left, right)

    def minNumberOperations(self, target):
        n = len(target)
        self.seg = [None] * (4 * n)
        self.build(0, 0, n - 1, target)

        ans = 0
        q = deque()
        q.append((0, n - 1, 0))  

        while q:
            l, r, level = q.popleft()
            mini, idx = self.query(0, 0, n - 1, l, r)
            ans += (mini - level)
            if idx - 1 >= l:
                q.append((l, idx - 1, mini))
            if idx + 1 <= r:
                q.append((idx + 1, r, mini))

        return ans
