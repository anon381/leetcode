class Solution:
    def possible(self, max_val: int, power: list[int], r: int, k: int) -> bool:
        n = len(power)
        extra = [0] * n
        for i in range(n):
            if i > 0:
                extra[i] += extra[i - 1]
            current = power[i] + extra[i]
            if current < max_val:
                diff = max_val - current
                if diff > k:
                    return False
                k -= diff
                extra[i] += diff
                ri = min(n - 1, i + 2 * r)
                if ri + 1 < n:
                    extra[ri + 1] -= diff
        return True

    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n
        for i in range(n):
            le = max(i - r, 0)
            ri = min(i + r, n - 1)
            power[le] += stations[i]
            if ri + 1 < n:
                power[ri + 1] -= stations[i]
        min_val = power[0]
        for i in range(1, n):
            power[i] += power[i - 1]
            min_val = min(min_val, power[i])
        low, high = 0, min_val + k
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(mid, power, r, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
