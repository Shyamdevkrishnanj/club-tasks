def diagonal_diff():
    a = int(input())
    arr = []
    for i in range(a):
        mat = list(map(int, input().rstrip().split()))
        arr.append(mat)
    
    s1 = 0
    s2 = 0
    for i in range(a):
        s1 += arr[i][i]
        s2 += arr[i][a-i-1]
    
    return abs(s1 - s2)
print(diagonal_diff())



 