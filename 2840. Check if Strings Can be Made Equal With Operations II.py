class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        prime = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
        ]

        mod = 10**9 + 7
        h1, h2 = [1, 1], [1, 1]

        for i in range(len(s1)):
            off = i & 1
            h1[off] = (h1[off] * prime[ord(s1[i]) - 97]) % mod
            h2[off] = (h2[off] * prime[ord(s2[i]) - 97]) % mod

        return h1 == h2
