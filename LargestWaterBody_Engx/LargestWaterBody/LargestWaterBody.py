island = []
with open("largeinput.txt") as f:
    for line in f:        
        island.append([int(i) for i in line if i in ['0','1']])
rows, cols = len(island), len(island[0])
visited = [[0 for i in range(cols)] for j in range(rows)]
def adjacent(i):
    possible_adjacent_nodes = [(i[0]-1, i[1]), (i[0]+1,i[1]), (i[0],i[1]-1), (i[0], i[1]+1)]
    return [i for i in possible_adjacent_nodes if 0<=i[0]<rows and 0<=i[1]<cols and island[i[0]][i[1]] == 0]
def BFS(node):
    q = [node]
    component_len = 0    
    while q:
        curr = q[0]
        del q[0]
        visited[curr[0]][curr[1]] = 1
        component_len += 1
        for adj in adjacent(curr):
            if visited[adj[0]][adj[1]] != 1:
                visited[adj[0]][adj[1]] = 1
                q.append(adj)
    return component_len
result = -1
for i in range(rows):
    for j in range(cols):
        if island[i][j] == 0 and visited[i][j] == 0:
            result = max(result, BFS((i,j)))
            print(result)        
print(result)