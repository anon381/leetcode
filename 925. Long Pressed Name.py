
# Complexity
# Time complexity:
# O(n), where n is the length of the typed string. This is because of a single loop that iterates through the typed string.

# Space complexity:
# O(1). The solution uses a constant amount of space for the pointers i and j, and does not use any additional data structures that grow with the input size.



class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
            
        return i == len(name)



# in cpp
