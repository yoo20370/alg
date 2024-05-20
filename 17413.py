string = input()

def reverseString(string) :
    stack = []
    resultList = []
    check = 0
    
    for word in string :

        if word == '<' :
            check = 1
            while len(stack) != 0 : 
                resultList.append(stack.pop())
            resultList.append(word)
            continue
            
        elif word == '>':
            check = 0
            resultList.append(word)
            continue
        elif word == ' ' :
            while len(stack) != 0 : 
                resultList.append(stack.pop())
            resultList.append(' ')
            continue

        if check == 0 :
            stack.append(word)
        
        elif check == 1 :
            resultList.append(word)
    while len(stack) != 0 : 
                resultList.append(stack.pop())

    for i in resultList :
         print(i, end="")

reverseString(string)
        
            