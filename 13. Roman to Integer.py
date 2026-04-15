class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}
        result = 0
        i =0
        while i < len(s):
            x = min(i + 1, len(s) - 1)
            while i < len(s):
                if s[i:i+2] in my_dict:
                    result += my_dict[s[i:i+2]]
                    i += 2
                else:
                    result += my_dict[s[i]]
                    i += 1
        return result
#       Intuition
# The idea is to convert a Roman numeral string into an integer by checking whether a character forms a valid two-character combination (like IV, IX, XL, etc.) or should be treated as a single symbol.

# Approach
# We use a dictionary that maps both single Roman symbols and special two-character combinations to their integer values.

# We iterate through the string using an index i. At each step:

# First, check if the substring s[i:i+2] exists in the dictionary (handles cases like IV, IX, etc.)
# If it exists, add its value and move i by 2
# Otherwise, add the value of s[i] and move i by 1

# This ensures we correctly handle subtraction cases in Roman numerals without complex comparisons.

# Complexity
# Time complexity: 𝑂(𝑛)
# We scan the string once, processing each character at most once or twice.
# Space complexity: O(1)
# The dictionary size is fixed and does not grow with input size.
