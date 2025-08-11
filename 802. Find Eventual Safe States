class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        visited=[0]*n
        def dfs(i):
            if visited[i]==1:
                return False
            elif visited[i]==2:
                return True
            else:
                visited[i]=1
                for j in graph[i]:
                    x=dfs(j)
                    if x==False:
                        return False
                visited[i]=2
                return True
        res=[]
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res 
