class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        # 1. Add implicit boundary fences
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)

        # 2. Sort fences
        hFences.sort()
        vFences.sort()

        # 3. Store all possible horizontal gaps
        hGaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                hGaps.add(hFences[j] - hFences[i])

        # 4. Check vertical gaps against horizontal gaps
        maxSide = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                gap = vFences[j] - vFences[i]
                if gap in hGaps:
                    maxSide = max(maxSide, gap)

        if maxSide == -1:
            return -1

        # 5. Return area modulo 1e9+7
        MOD = 10**9 + 7
        return (maxSide * maxSide) % MOD
