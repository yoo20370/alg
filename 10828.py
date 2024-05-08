
N = int(input())

stack = []
inputList = []
for i in range(N) :
    data = input()
    inputList.append(data)

s_top = 0    

def push(n) :
    global s_top
    stack.append(n)
    s_top = s_top + 1

def pop() :
    global s_top
    if(s_top == 0) :
        print(-1)
        return
    print(stack.pop())
    s_top = s_top - 1
    
def top() :
    global s_top
    if s_top == 0 :
        print(-1)
        return
    print(stack[s_top-1])

def size() :
    global s_top
    print(s_top)

def empty() :
    global s_top
    if s_top == 0 :
        print(1)
    else :
        print(0)

for i in inputList :
    if i.find('push') != -1 :
        command, num = i.split(' ')
        push(int(num))
    elif i in 'pop' :
        pop()
    elif i in 'size' :
        size()
    elif i in 'empty' :
        empty()
    elif i in 'top' :
        top()
    
