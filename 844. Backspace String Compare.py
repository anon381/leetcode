# Complexity
# Time complexity: O(max(len(s),len(t))
# Space complexity: O(1)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack
        return remove_characters(s) == remove_characters(t)


#in cpp
