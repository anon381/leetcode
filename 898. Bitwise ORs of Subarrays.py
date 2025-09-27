class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        result_ors = set()
        current_ors = set()
        for x in arr:
            next_ors = {x | y for y in current_ors}
            next_ors.add(x)            
            result_ors.update(next_ors)            
            current_ors = next_ors
        return len(result_ors)
