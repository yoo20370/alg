from collections import deque

def peek(stack) :
    if len(stack) == 0 :
        return -1 
    else :
        return stack[len(stack) - 1]
    
def algFunc() :
    stack = deque()
    stickCnt = 0
    inputData = input()

    for n in inputData : 
        if n == '(' :
            if len(stack) != 0 :
                stickCnt += 1
                stack.append(n)
        elif n == ')' :
            if peek(stack) == '(' :
                print('레이저')
            stickCnt -= 1
            stack.pop()
            