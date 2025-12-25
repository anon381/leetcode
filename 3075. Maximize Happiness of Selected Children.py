class Solution:
    def maximumHappinessSum(self, christmasJoy: List[int], gifts: int) -> int:
        christmasJoy.sort(reverse=True)
        
        totalJoy = 0
        for turn in range(gifts):
            currentJoy = christmasJoy[turn] - turn
            if currentJoy <= 0:
                break
            totalJoy += currentJoy
        
        return totalJoy
