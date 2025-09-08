class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        one = []
        two = []
        three = []
        for i in digits:
            if i % 3 == 1:
                one.append(str(i))
            elif i % 3 == 2:
                two.append(str(i))
            else:
                three.append(str(i))
        one.sort()
        two.sort()
        one = one[::-1]
        two = two[::-1]
        if sum(digits) % 3 == 1:
            try:
                one.pop()
            except:
                two.pop()
                two.pop()
        elif sum(digits) % 3 == 2:
            try:
                two.pop()
            except:
                one.pop()
                one.pop()
        ans = "".join(one)
        ans += "".join(two)
        ans += "".join(three)
        
        if ans == "":
            return ""
        if ans[0] == "0":
            return "0"
        ans = "".join(sorted(ans))[::-1]
        return ans

