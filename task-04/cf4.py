inp =int(input())
n = 0
for i in range(inp):
    k = input()
    if k[0] == '+' or k[1] == '+':
        n+=1
    else:
        n-=1
print(n)