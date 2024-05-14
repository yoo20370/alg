from collections import deque
N = int(input())

inputList = []
for i in range(N) :
    inputList.append(input())

def size(queue) :
    return len(queue)

def push(queue, val) :
    queue.append(val)

def pop(queue) :
    if size(queue) == 0 :
        return -1
    return queue.popleft()

def empty(queue) :
    if size(queue) == 0 :
        return 1
    else :
        return 0

def front(queue) :
    if size(queue) == 0 :
        print(-1)
    else :
        print(queue[0])


def back(queue) :
    if size(queue) == 0 :
        print(-1)
    else :
        print(queue[size(queue) - 1])

def queueFunc() :
    queue = deque()

    for command in inputList :
        if not command.find('push') :
            comm, val = command.split(' ')
            push(queue, val)
        elif not command.find('pop') :
            print(pop(queue))
        elif not command.find('empty') :
            print(empty(queue))
        elif not command.find('size') :
            print(size(queue))
        elif not command.find('front') :
            front(queue)
        elif not command.find('back') :
            back(queue)

queueFunc()