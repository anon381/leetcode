Complexity
Time Complexity : O(N∗X∗Log(N))
Space Complexity : O(N)

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        freq = defaultdict(int)
        ans = []

        def key(val):
            return (freq[val], val)

        topX = SortedList(key=key)
        rest = SortedList(key=key)
        sumTop = 0


        def rebalance():
            nonlocal sumTop
            while len(topX) < min(x, len(freq)) and rest:
                best = rest.pop(-1)
                topX.add(best)
                sumTop += freq[best] * best
            while len(topX) > x:
                worst = topX.pop(0)
                sumTop -= freq[worst] * worst
                rest.add(worst)
            while topX and rest:
                worstTop = topX[0]
                bestRest = rest[-1]
                if (freq[bestRest] > freq[worstTop] or
                   (freq[bestRest] == freq[worstTop] and bestRest > worstTop)):
                    topX.remove(worstTop)
                    rest.remove(bestRest)
                    topX.add(bestRest)
                    rest.add(worstTop)
                    sumTop += freq[bestRest] * bestRest - freq[worstTop] * worstTop
                else:
                    break

        for i, v in enumerate(nums):
            if freq[v] > 0:
                if v in topX:
                    topX.remove(v)
                    sumTop -= freq[v] * v
                else:
                    rest.remove(v)
            freq[v] += 1
            rest.add(v)
            rebalance()

            if i >= k:
                u = nums[i - k]
                if u in topX:
                    topX.remove(u)
                    sumTop -= freq[u] * u
                else:
                    rest.remove(u)
                if freq[u] == 1:
                    del freq[u]
                else:
                    freq[u] -= 1
                    rest.add(u)
                rebalance()

            if i >= k - 1:
                ans.append(sumTop)

        return ans
