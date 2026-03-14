class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        pointer1, idx1, pointer2, idx2 = 0, 0, 0, 0  # Pointers and indices for both words

        while pointer1 < len(word1) and pointer2 < len(word2):
            # Get the current characters from both words
            char1, char2 = word1[pointer1][idx1], word2[pointer2][idx2]

            # Compare characters
            if char1 != char2:
                return False

            # Move to the next character in the current word
            idx1 += 1
            idx2 += 1

            # Move to the next word if the end of the current word is reached
            if idx1 == len(word1[pointer1]):
                idx1, pointer1 = 0, pointer1 + 1 # Move to the next word in word1

            if idx2 == len(word2[pointer2]):
                idx2, pointer2 = 0, pointer2 + 1 # Move to the next word in word2

        # Check if both pointers have reached the end of their respective arrays
        return pointer1 == len(word1) and pointer2 == len(word2)        
