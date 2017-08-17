#63-->0.0275313
#63   0.0275313125

#Smallest sum with maximum probability: 63
#Highest Probability : 0.0275313125

def findWays(m, n, x):
    matrix = [[0 for i in range(x+1)] for j in range(n+1)]		
    for j in range(1,x):
        if j<=m and j<=x:
            matrix[1][j] = 1	
    for i in range(2,n+1):
        for j in range(1,x+1):
            for k in range(1,x):
                if k<=m and k<j:
                    matrix[i][j] += matrix[i-1][j-k]
    return matrix[-1]
res = findWays(20,6,121)
total = pow(20,6)
print(res.index(max(res)), max(res)/total)


# Probabilistic approach
#import random
#face_range = 4
#num_dice = 3
#trails = 100000
#dic = {i:0 for i in range(num_dice,num_dice*face_range+1)}
#for i in range(trails):
#    curr_sum = 0
#    for j in range(num_dice):
#        curr_sum += random.randint(1,face_range)
#    dic[curr_sum]+=1    
#for key in dic:
#    print(key, dic[key]/100000)