data = input()
N = int(input())

string = [i for i in data]

commandList = []
for i in range(N) :
    commandList.append(input())
stack = []
def editor() :

    for command in commandList :
        if not command.find('P') :
            com, val = command.split(' ')
            string.append(val)
        elif not command.find('L') :
            if len(string) == 0 :
                continue
            temp = string.pop()
            stack.append(temp)
        elif not command.find('D') :
            if len(stack) == 0 :
                continue
            string.append(stack.pop())
        elif not command.find('B') :
            if len(string) == 0 :
                continue
            string.pop()
    while len(stack) > 0 :
        string.append(stack.pop())
    for i in string :
        print(i, end="")
   
editor()