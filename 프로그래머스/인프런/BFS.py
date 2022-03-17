from collections import deque

#BFS
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

b


