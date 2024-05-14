from collections import deque
N, K = map(int, input().split())

queue = deque()
for i in range(1, N+1) : 
    queue.append(i)

result_list = list()
def func(queue) :
    while len(queue) != 0 :
        for _ in range(K-1) :
            temp = queue.popleft()
            queue.append(temp)
        result_list.append(queue.popleft())
    
    print("<",end="")
    print(", ".join(map(str,result_list)),end="")
    print(">")
    
func(queue)

    


