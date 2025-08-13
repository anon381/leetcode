class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack: 
                return False
            if code[i:i+9] == "<![CDATA[": 
                j = i + 9
                i = code.find("]]>", j)
                if i == -1:
                    return False
                i += 3
            elif code[i:i+2] == "</":  
                j = i + 2
                i = code.find(">", j)
                if i == -1 or not stack or stack.pop() != code[j:i] or '<' in code[j:i] or ' ' in code[j:i]:
                    return False
                i += 1
            elif code[i] == "<":  
                j = i + 1
                i = code.find(">", j)
                if i == -1 or not (1 <= i - j <= 9) or not code[j:i].isupper() or '<' in code[j:i] or ' ' in code[j:i]:
                    return False
                stack.append(code[j:i])
                i += 1
            else:  
                i += 1
        return not stack
