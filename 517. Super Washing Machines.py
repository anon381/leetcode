class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        ave, rem = divmod(sum(machines),len(machines))   
        if rem: return -1                                
        machines = [m - ave for m in machines]          
        return max(max(machines), max(map(abs,(accumulate(machines)))))  
