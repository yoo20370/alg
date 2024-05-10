from collections import deque
N = int(input())

inputList = deque()
for _ in range(N) :
    inputList.append(int(input()))

stack = [0]
resultList = []
def fun() :
    global inputList
    num = 0
    numList = []
    while len(inputList) != 0 :
        cur = inputList.popleft()
        if num < cur :
            while num != cur : 
                numList.append(num)
                num += 1
                stack.append(num)
                resultList.append("+")
            # resultList.append("+")
            resultList.append("-")
            stack.pop()
                
        else : 
            if len(stack) == 1 :
                print("NO")
                return
            if stack[len(stack)-1] == cur :
                resultList.append("-")
                stack.pop()
                continue  
            while len(stack) != 1 :
                if stack.pop() == cur :
                    resultList.append("-")
                    break
                else :
                    resultList.append("-")
                
    for i in resultList :
        print(i)

fun()

        


        

    