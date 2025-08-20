class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            try:
                res.append(int(operations[i]))
            except ValueError:
                if operations[i] == "+":
                    res.append(res[-2] + res[-1])
                elif operations[i] == "D":
                    res.append(res[-1] * 2)
                elif operations[i] == "C":
                    res.pop()  
        return sum(res)
## or 
class Solution(object):
    def calPoints(self, operations):
        lst = []

        for i in operations:
            if i == "C":
                lst.pop()
            elif i == "D":
                lst.append(2 * lst[-1])
            elif i == "+":
                lst.append(lst[-1] + lst[-2])
            else:
                lst.append(int(i))

        return sum(lst)
