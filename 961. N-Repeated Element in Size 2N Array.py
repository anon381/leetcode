class Solution:
    def repeatedNTimes(self, A):
        while 1:
            s = random.sample(A, 2)
            if s[0] == s[1]:
                return s[0]        