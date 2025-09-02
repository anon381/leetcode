class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        left = 0 
        return_list = []
        S += '1'
        for index, letter in enumerate(S):
            if letter != S[left]:
                if index - left >= 3:
                    return_list.append([left, index - 1])
                left = index
        return return_list
