
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        probs = [0.0] * maxPts
        probs[0] = 1.0

        running_sum = 1.0
        answer = 0.0

        for card_total in range(1, n + 1):
            current_prob = running_sum / maxPts

            if card_total < k:
                running_sum += current_prob
            else:
                answer += current_prob

            if card_total >= maxPts:
                running_sum -= probs[card_total % maxPts]

            probs[card_total % maxPts] = current_prob

        return answer
