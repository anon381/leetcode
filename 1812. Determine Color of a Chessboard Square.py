class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter = coordinates[0]
        num = coordinates[1]
        if ord(letter) % 2 == 0:
            return int(num) % 2 != 0
        else:
            return int(num) % 2 == 0


#in cpp
