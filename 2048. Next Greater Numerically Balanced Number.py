
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def balanced(x):
            freq = Counter(str(x))
            for key, val in freq.items():
                if int(key) != val:
                    return False
            return True

        num = n + 1
        while True:
            if balanced(num):
                return num
            num += 1
