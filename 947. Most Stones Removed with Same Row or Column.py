
class Solution:
    def __init__(self):
        self.component_count = 0

    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [0] * 20003
        for x, y in stones:
            self.union(x + 1, y + 10002, parent)
        return len(stones) - self.component_count

    def find(self, node: int, parent: List[int]) -> int:
        if parent[node] == 0:
            parent[node] = node
            self.component_count += 1
        if parent[node] != node:
            parent[node] = self.find(parent[node], parent)
        return parent[node]

    def union(self, node_a: int, node_b: int, parent: List[int]) -> None:
        rep_a = self.find(node_a, parent)
        rep_b = self.find(node_b, parent)
        if rep_a != rep_b:
            parent[rep_b] = rep_a
            self.component_count -= 1
