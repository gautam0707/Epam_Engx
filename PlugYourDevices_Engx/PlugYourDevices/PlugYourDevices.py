n, k, m = 5, 3, 0  
sockets = []    
with open("smallinput.txt", 'r') as f:
    for line in f:
        coord = line.replace(")("," ")[1:-1].split()
        m = len(coord)
        for i in coord: 
            print(i,end=" ")           
            x,y = [int(j) for j in i.split(',')]
            if y == 0:
                sockets.append(x)
            elif x == n:
                sockets.append(n + y)
            elif y == n:
                sockets.append(n * 3 - x)
            else:
                sockets.append(n * 4 - y)   
print()
print(sockets)
sockets = sorted(sockets) 
sockets = sockets + [i + 4*n for i in sockets] 
print(sockets)  
mn = 999999999
for i in range(len(sockets)-k+1):
    t = sockets[i+k-1]-sockets[i]
    print(sockets[i+k-1], sockets[i])
    if t < mn:
        mn = t
print(mn)