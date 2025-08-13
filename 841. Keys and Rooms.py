class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        def dfs(room):
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    dfs(key)
        dfs(0)
        return all(visited)
