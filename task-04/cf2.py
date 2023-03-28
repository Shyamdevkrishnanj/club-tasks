n=int(input())

list = []

for _ in range(n):
    list.append(input())


for i in range (len(list)):
     if (len(list[i])>10):
          
           print(((list[i])[0])+str((len(list[i]))-2)+(list[i])[-1])
     else:
          print(list[i])

# n = int(input())
# list = []

# for i in range(n):
#     list.append(input())

# for i in range (len(list)):
# 	if (len(list[i])>10):
        
#         print(((list[i])[0])+str((len(list[i]))-2)+(list[i])[-1])
    
#     else:
#         print(list[i])