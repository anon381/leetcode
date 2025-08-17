

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        total = len(quiet)
        network = [[] for _ in range(total)]
        incoming = [0] * total
        output = list(range(total))
        
        for x, y in richer:
            network[x].append(y)
            incoming[y] += 1
        
        dq = deque()
        for person in range(total):
            if incoming[person] == 0:
                dq.append(person)
        
        while dq:
            current = dq.popleft()
            
            for nxt in network[current]:
                if quiet[output[current]] < quiet[output[nxt]]:
                    output[nxt] = output[current]
                
                incoming[nxt] -= 1
                if incoming[nxt] == 0:
                    dq.append(nxt)
        
        return output
