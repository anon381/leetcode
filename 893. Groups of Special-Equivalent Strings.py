
class Solution:
    def numSpecialEquivGroups(self, A):
        s = set()

        for w in A:
            even = []
            odd = []

            for i, ch in enumerate(w):
                if i % 2 == 0:
                    even.append(ch)
                else:
                    odd.append(ch)

            even.sort()
            odd.sort()

            s.add(("".join(even), "".join(odd)))

        return len(s)
