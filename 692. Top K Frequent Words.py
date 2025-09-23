class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        # Step 1: Count word frequencies
        freq = Counter(words)

        # Step 2: Sort by frequency desc, then lex asc
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Step 3: Return top k
        return [word for word, count in sorted_words[:k]]
