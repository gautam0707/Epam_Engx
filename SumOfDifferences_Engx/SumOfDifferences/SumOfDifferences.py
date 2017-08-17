numbers = [int(i) for i in open('input.txt','r').read().split(',')]
index = result = prev = 0
while index < len(numbers)-1:    
    while index < len(numbers)-1 and numbers[index] <= numbers[index+1]:
        index += 1
    if prev<index:
        result += numbers[index] - numbers[prev]                
    while index < len(numbers)-1 and numbers[index] >= numbers[index+1]:
        index += 1
    prev = index
print(result)


