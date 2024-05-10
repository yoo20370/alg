from collections import deque

N = int(input())

inputList = list()
for i in range(N) :
    inputList.append(input())

for stage in inputList :
    stack = []
    for i in stage :
        if i == ')' :
            if len(stack) == 0 :
                print("NO")
                break
            stack.pop()
            continue
        stack.append(i)
    else:
        if len(stack) != 0 :
            print("NO")
            continue
        else : 
            print("YES")

