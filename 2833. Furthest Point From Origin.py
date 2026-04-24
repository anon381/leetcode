class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x, r=0, 0
        for c in moves:
            x+=(c=='R')-(c=='L')
            r+=c=='_'
        return abs(x)+r
