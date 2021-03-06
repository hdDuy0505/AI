import numpy as np

def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 

    path = []
    visited = {}
    visited[start] = -1
    stack = []
    stack.append(start)
    while stack:
        temp = stack[len(stack)-1]
        if end == temp:
            break
        check = True  #Kiểm tra vị trí đó còn đỉnh nào chưa đi qua hay không           
        for i in range(len(matrix[temp])):
            if matrix[temp][i] != 0 and i not in visited:
                visited[i] = temp
                stack.append(i)
                check = False
                break
        if check: #True: đã đi qua hết các đỉnh khác mà đỉnh đó có thể đi qua => loại đỉnh đó ra stack
            stack.pop()

    if end in visited:
        path.append(end)
        while visited[end] != -1:
            path.insert(0, visited[end])
            end = visited[end]
    
    return visited, path

def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path = []
    visited = {}
    visited[start] = -1
    queue = []
    queue.append(start)
    while queue:
        temp = queue.pop()
        if end == temp:
            break
        for i in range(len(matrix[temp])):
            if matrix[temp][i] != 0 and i not in visited:
                 queue.insert(0, i)
                 visited[i] = temp
    
    if end in visited:
        path.append(end)
        while visited[end] != -1:
            path.insert(0, visited[end])
            end = visited[end]
    
    return visited, path

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  

    path = []
    visited = {}
    distance = {} #Lưu các đường đi đang xét tại các bước

    visited[start] = -1
    if start == end:
        return visited, path
    
    distance[start] = [start, -1] #value[0]: Lưu đỉnh kề trước đó đi tới, value[1]: lưu khoảng cách từ start đó tới đỉnh đó

    cost = 0 #Dùng lưu khoảng cách mỗi bước làm tại vị trí đang xét với vị trí start
    targetVetex = start #Dùng lưu đỉnh đang xét

    while distance and end not in visited:      
        for i in range(len(matrix[0])):
            if matrix[targetVetex][i] != 0 and i not in visited: #Đỉnh đó có đường đi và vẫn chưa trong tập đỉnh đi qua(visited)
                if i not in distance:
                    distance[i] = [targetVetex, matrix[targetVetex][i] + cost]
                else:
                    if distance.get(i)[1] > matrix[targetVetex][i] + cost: #Nếu K/c đang xét nhỏ hơn K/c mà đi tới đỉnh đó trong dic, ta cập nhật lại k/c
                        distance[i] = [targetVetex, matrix[targetVetex][i] + cost]

        del distance[targetVetex] #Xóa đường đi đã lựa chọn ra khỏi distance
        if len(distance) > 0:
            targetVetex = list(distance.keys())[0] #Lấy đỉnh đầu tiên trong dictionary để khởi tạo tìm giá trị nhỏ nhất
            vetexLast = list(distance.values())[0][0] #Lấy đỉnh đã đi trước khi tới đỉnh đầu tiên trong dic
            minDistance = list(distance.values())[0][1] #Lấy giá trị k/c đầu tiên của dic

            for key, value in distance.items():
                if minDistance > value[1]:#value[0]: Lưu đỉnh trước đó đi tới, value[1]: lưu khoảng cách
                    targetVetex = key
                    vetexLast = value[0]
                    minDistance = value[1]
            cost = minDistance
            visited[targetVetex] = vetexLast
   
    if end in visited:
        path.append(end)
        while visited[end] != -1:
            path.insert(0, visited[end])
            end = visited[end]

    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path = []
    visited = {}
    distance = {} #Lưu các đường đi đang xét tại các bước

    visited[start] = -1
    if start == end:
        return visited, path
    
    distance[start] = [start, -1] #value[0]: Lưu đỉnh trước đó, value[1]: lưu khoảng cách
    
    targetVetex = start
    while distance and end not in visited: 

        del distance[targetVetex] #Xóa đường đi đã lựa chọn ra khỏi distance
        for i in range(len(matrix[0])):
            if matrix[targetVetex][i] != 0 and i not in visited: #Đỉnh đó có đường đi và vẫn chưa trong tập đỉnh đi qua(visited)
                if i not in distance: 
                    distance[i] = [targetVetex, matrix[targetVetex][i]]
                else: 
                    if distance.get(i)[1] > matrix[targetVetex][i]: #Nếu K/c đang xét nhỏ hơn K/c mà đi tới đỉnh đó trong dic, ta cập nhật lại k/c
                        distance[i] = [targetVetex, matrix[targetVetex][i]]

        if len(distance) > 0:
            targetVetex = list(distance.keys())[0] #Lấy đỉnh đầu tiên trong dictionary để khởi tạo tìm giá trị nhỏ nhất
            vetexLast = list(distance.values())[0][0] #Lấy đỉnh đã đi trước khi tới đỉnh đầu tiên trong dic
            minDistance = list(distance.values())[0][1] #Lấy giá trị k/c đầu tiên của dic

            for key, value in distance.items():
                if minDistance > value[1]:#value[0]: Lưu đỉnh trước đó, value[1]: lưu khoảng cách
                    targetVetex = key
                    vetexLast = value[0]
                    minDistance = value[1]
            visited[targetVetex] = vetexLast

    if end in visited:
        path.append(end)
        while visited[end] != -1:
            path.insert(0, visited[end])
            end = visited[end]
    
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path = []
    visited = {}
    h = {} #heuristic
    distance = {} #Lưu các đường đi đang xét tại các bước
    for key, value in pos.items():
        h[key] = np.sqrt((value[0] - pos[end][0])**2 + (value[1] - pos[end][1])**2)
    
    visited[start] = -1
    if start == end:
        return visited, path
    
    distance[start] = [start, -1, -1] #value[0]: lưu đỉnh trước kề, value[1]: lưu k/c có hereutic,
                                      #value[2]: lưu k/c ko có hereutic tính từ đỉnh start tới đỉnh đang xét 
    targetVetex = start #Đỉnh đang xét
    cost = 0 #Dùng lưu khoảng cách mỗi bước làm tại vị trí đang xét
    while distance and end not in visited:
        for i in range(len(matrix[0])):
            if matrix[targetVetex][i] != 0 and i not in visited:
                if i not in distance:
                    distance[i] = [targetVetex, matrix[targetVetex][i] + h[i] + cost, matrix[targetVetex][i] + cost]
                else:
                    if distance.get(i)[1] > matrix[targetVetex][i] + cost + h[i]:
                        distance[i] = [targetVetex, matrix[targetVetex][i] + h[i] + cost, matrix[targetVetex][i] + cost]

        del distance[targetVetex] #Xóa đường đi đã lựa chọn trước đó ra khỏi distance
        if len(distance) > 0:
            targetVetex = list(distance.keys())[0] #Lấy đỉnh đầu tiên trong dictionary để khởi tạo tìm giá trị nhỏ nhất
            vetexLast = list(distance.values())[0][0] #Lấy đỉnh đã đi trước khi tới đỉnh đầu tiên trong dic
            minDistance = list(distance.values())[0][1] #Lấy giá trị k/c có hereutic đầu tiên của dic
            costMin = list(distance.values())[0][2] #Dùng lưu khoảng cách của phần tử dic đầu tiên đến vị trí start

            for key, value in distance.items():
                if minDistance > value[1]:  
                    targetVetex = key
                    vetexLast = value[0]
                    minDistance = value[1]
                    costMin = value[2]

            cost = costMin
            visited[targetVetex] = vetexLast
    
    if end in visited:
        path.append(end)
        while visited[end] != -1:
            path.insert(0, visited[end])
            end = visited[end]
    
    return visited, path