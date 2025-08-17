from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x_idx):
            if parent[x_idx] == x_idx:
                return x_idx
            parent[x_idx] = find(parent[x_idx])
            return parent[x_idx]

        parent = list(range(26))

        for eq in equations:
            if eq[1] == '=':
                a_idx = ord(eq[0]) - ord('a')
                b_idx = ord(eq[3]) - ord('a')
                parent[find(a_idx)] = find(b_idx)

        for eq in equations:
            if eq[1] == '!':
                a_idx = ord(eq[0]) - ord('a')
                b_idx = ord(eq[3]) - ord('a')
                if find(a_idx) == find(b_idx):
                    return False

        return True
