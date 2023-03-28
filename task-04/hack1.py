# # def compare(a,b):
# #     point = [0,0]
    
# #     for i in range(0,3):
# #         if a[i] > b[i]:
# #             point[0] = point[0]+1
# #         elif a[i] < b[i]:
# #             point[1] = point[1]+1
# #         else:
# #             pass
# #         return point
    
# # a[0], a[1],a[2] = input("enter a: ").split()
# # b = input("enter b: ")

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_pnt = 0
b_pnt = 0

for i in range(len(a)):
    if a[i] > b[i]:
        a_pnt += 1
    elif a[i] < b[i]:
        b_pnt +=1
    else:
        pass

print(a_pnt, b_pnt)