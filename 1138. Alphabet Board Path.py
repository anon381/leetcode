Complexity
Time complexity: O(N)
Space complexity: O(1)

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        current_indx = [0,0]
        alphabet_hashMap = {}
        letters = [
                    ['a', 'b', 'c', 'd', 'e'],
                    ['f', 'g', 'h', 'i', 'j'],
                    ['k', 'l', 'm', 'n', 'o'],
                    ['p', 'q', 'r', 's', 't'],
                    ['u', 'v', 'w', 'x', 'y'],
                    ['z', '', '', '', '']
                ]
        for i in range(len(letters)):
            for j in range(len(letters[0])):
                if letters[i][j] != '':
                    alphabet_hashMap[letters[i][j]] = [i, j]
        path = ""
        for i in target:
            x , y =  alphabet_hashMap[i]

            if current_indx[0] == x and current_indx[1] == y:
                path += "!"
                continue

            if current_indx[1] > y:
                direction = "L"*(current_indx[1] - y)
                path += direction

            if x > current_indx[0]:
                direction = "D"*(x - current_indx[0])
                path += direction

            if current_indx[0] > x:
                direction = "U"*(current_indx[0] - x)
                path += direction

            if y > current_indx[1]:
                direction = "R"*(y - current_indx[1])
                path += direction

            current_indx[0] = x
            current_indx[1] = y
            path += "!"
            
        return path
