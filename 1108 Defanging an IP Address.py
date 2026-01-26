class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
    def defangIPaddr(self, address: str) -> str:
        return re.sub('\.', '[.]', address)
    def defangIPaddr(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)        
