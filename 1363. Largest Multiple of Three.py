class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        def bucket_sorted(arr):
            c = collections.Counter(arr)
            return [x for i in range(10) if i in c for x in [i]*c[i]]
        
        d = collections.defaultdict(list)
        for n in digits:
            d[n%3] += n,
        res, short, long = d[0], *sorted((d[1], d[2]), key=len)
        short, long = bucket_sorted(short), bucket_sorted(long)
        
        if (len(long) - len(short)) % 3 > abs((len(long) % 3) - (len(short) % 3)):
            short, long = (short, long) if len(short)%3 < len(long)%3 else (long, short)
            res += short + long[abs(len(short)%3 - len(long)%3):]
        else:
            res += short + long[(len(long)-len(short))%3:]
            
        res = bucket_sorted(res)[::-1]
        return '0' if res and not res[0] else ''.join(map(str, res))