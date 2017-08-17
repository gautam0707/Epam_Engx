# this is wrong answer, need to update solution!
inp = []
with open('TextFile1.txt','r') as file:
    for line in file:
        inp+=[int(i) for i in line.split(',')]
minval = min(inp[:5])
result = minval
for i in range(1,len(inp)-5+1):
    if minval not in inp[i:i+5]:
        minval = min(inp[i:i+5])
        result+=minval
print(result)
