def algFunc() :
    N, M = map(int, input().split())
    inputList = []
    for _ in range(N) : 
        row = list(map(int, input().split()))
        inputList.append(row)

    print(inputList)
algFunc()