
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
