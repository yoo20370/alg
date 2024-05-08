from collections import deque

def reverse(aList) :
    stack = deque()
    temp = ""
    for i in aList :
        stack.append(i)
    
    for i in range(len(stack)) :
        temp += stack.pop()

    return temp

N = int(input())

strList = list()
for i in range(N) :
    strList.append(input())

result = ""
tempList = list()
for strs in strList :
    preList = strs.split(' ')
    for word in preList :
        temp = reverse(word)
        tempList.append(temp)
    result = " ".join(tempList)
    print(result)
    tempList = list()



