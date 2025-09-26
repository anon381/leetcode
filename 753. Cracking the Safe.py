class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ava_edge = defaultdict(lambda: k-1)
        res = ['0'] * (n-1)
        suffix = ''.join(res)
        while ava_edge[suffix] >= 0:
            res.append(str(ava_edge[suffix]))
            ava_edge[suffix] -= 1
            suffix = ''.join(res[1-n:] if n > 1 else [])
        return ''.join(res)
