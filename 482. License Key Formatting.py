
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        S = S.replace('-', '')
        
        head = len(S) % K
        
        grouping = []

        if head:
            grouping.append( S[:head] )

        for index in range(head, len(S), K ):
            grouping.append( S[ index : index+K ] )

        return '-'.join( grouping ).upper()
        
## or 

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for ch in s:
            if ch == '-':
                continue
            chars.append(ch.upper())

        result = []
        count = 0
        for ch in reversed(chars): #reverse chars
            if count == k:
                result.append('-')
                count = 0
            result.append(ch)
            count += 1
        return ''.join(reversed(result))
