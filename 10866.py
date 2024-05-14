N = int(input())

def push_front(val, deque) :
    if len(deque) == 0 :
        deque.append(val)
    else : 
        stack = []
        # 덱에서 꺼내서 스택에 저장 
        while len(deque) != 0 : 
            stack.append(deque.pop())
        deque.append(val)
        while len(stack) != 0 :
            deque.append(stack.pop())

commandList = []
for _ in range(N) :
    commandList.append(input())

def func10866(commandList) :
    deque = []

    for command in commandList :
        if not command.find('push_back') :
            com, val = command.split(' ')
            deque.append(val) 
        elif not command.find('push_front') :
            com, val = command.split(' ')
            if len(deque) == 0 :
                deque.append(val)
            else : 
                stack = []
                # 덱에서 꺼내서 스택에 저장 
                while len(deque) != 0 : 
                    stack.append(deque.pop())
                deque.append(val)
                while len(stack) != 0 :
                    deque.append(stack.pop())
        elif not command.find('pop_front') :
            if len(deque) == 0 :
                print("-1")
            else : 
                stack = []
                while len(deque) != 0 : 
                    stack.append(deque.pop())
                print(stack.pop())
                while len(stack) != 0 :
                    deque.append(stack.pop())
        elif not command.find('pop_back') :
            if len(deque) == 0 :
                print("-1")
            else : 
                print(deque.pop())
        elif not command.find('size') :
            print(len(deque))
        elif not command.find('empty') :
            if len(deque) == 0 :
                print(1)
            else : 
                print(0)
        elif not command.find('front') :
            if len(deque) == 0 :
                print("-1")
            else : 
                print(deque[0])
        elif not command.find('back') :
            if len(deque) == 0 :
                print("-1")
            else : 
                print(deque[len(deque)-1])

func10866(commandList)