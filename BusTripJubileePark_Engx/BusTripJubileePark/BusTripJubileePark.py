matrix = []
with open("largeinput.txt","r") as f:
    for line in f:
        matrix.append([int(_) for _ in line.strip('[').strip(']\n').split(',')])
l = len(matrix)
adjacency_matrix = []
corners = [(0,0),(0,l-1),(l-1,0),(l-1,l-1)]
visited = [[0 for i in range(l)] for j in range(l)]
trace_path = [[(0,0) for i in range(l)] for j in range(l)]
for i in corners:
    trace_path[i[0]][i[1]] = (-1,-1)
def build_adjacency():
    for i in range(l):
        row_adjacency = []
        for j in range(l):
            N = matrix[i][j]
            x1, y1 = i-N, j
            x2, y2 = i, j-N
            x3, y3 = i+N, j
            x4, y4 = i, j+N
            possible_next_stops = [_ for _ in [(x1,y1), (x2,y2), (x3,y3), (x4,y4)] if 0<=_[0]<l and 0<=_[1]<l]
            row_adjacency.append(possible_next_stops)
        adjacency_matrix.append(row_adjacency)
build_adjacency()

def print_traced_path():
    curr = (l//2,l//2)
    path = [curr]    
    while trace_path[curr[0]][curr[1]] != (-1,-1):          
          curr = trace_path[curr[0]][curr[1]]          
          path.append(curr)    
    print("[",end="")
    print(path[-1],end="")
    for node in path[::-1][1:]:        
        print("->"+str(node),end="")
    print("]")

def run_queue(start):
    q = [(start,0)]   
    curr = q[0]       
    visited[curr[0][0]][curr[0][1]] = 1
    while q:
        curr = q[0]
        del q[0]        
        if curr[0] == (l//2,l//2):
            print_traced_path();
            return curr[1]+1
        for i in adjacency_matrix[curr[0][0]][curr[0][1]]:   
            if visited[i[0]][i[1]]!=1:
                q.append(((i[0],i[1]),curr[1]+1))
                visited[i[0]][i[1]] = 1
                trace_path[i[0]][i[1]] = (curr[0][0],curr[0][1])
    return 9999

for corner in corners:
    visited = [[0 for i in range(l)] for j in range(l)]
    print(corner, run_queue(corner))

#time2 = time.time()
#print(time2-time1)



########################## method 2

#def get_min_dist_path(start):
#    visited[start[0]][start[1]]=1
#    if start == (l//2,l//2):
#        return 1,(l//2,l//2)
#    else:        
#        N = matrix[start[0]][start[1]]
#        x1, y1 = start[0]-N, start[1]
#        x2, y2 = start[0], start[1]-N
#        x3, y3 = start[0]+N, start[1]
#        x4, y4 = start[0], start[1]+N
#        possible_next_stops = [_ for _ in [(x1,y1), (x2,y2), (x3,y3), (x4,y4)] if 0<=_[0]<l and 0<=_[1]<l and visited[_[0]][_[1]]==0]
#        #print(start, "********" ,possible_next_stops)
#        if not possible_next_stops:
#            return 99999,(None,None)
#        next_possibilites = []
#        next_sums = []
#        for i in possible_next_stops:
#            res,paths = get_min_dist_path(i)
#            next_sums.append(res)
#            next_possibilites.append(paths)
#        min_index = next_sums.index(min(next_sums))
#        return min(next_sums)+1, next_possibilites[min_index]
##        return min(map(get_min_dist_path, possible_next_stops))+1
## print((0,0), get_min_dist_path((0,0)))
#for corner in corners:
#    print(corner, get_min_dist_path(corner))
#    visited = [[0 for i in range(l)] for j in range(l)]

###Path : [(0, 0) -> (7, 0) -> (16, 0) -> (17, 0) -> (17, 7) -> (11, 7) -> (1, 7) ->(1, 3) -> (9, 3)- >(9, 9)]
###Number of halts = 10

#time2 = time.time()
#print(time2-time1)
