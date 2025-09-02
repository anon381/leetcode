# Complexity
# Time complexity: O(n)

# Space complexity: O(n)


class Solution(object):
    def reverseOnlyLetters(self, s):
        arr = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not arr[left].isalpha():
                left += 1
            while left < right and not arr[right].isalpha():
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return ''.join(arr)
