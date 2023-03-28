num = input()
integers = []
num_list = []
count = 0


cont_list = num.split()

for i in range (len(cont_list)):
        integers .append(cont_list[i])
   
num_sequence = input()

num_list = num_sequence.split()


cont_list = list(map(int, cont_list))
num_list = list(map(int, num_list))


temp = num_list[(cont_list[1])-1]
count=0
for i in range(0,len(num_list)):
    if num_list[i]>=temp and num_list[i]>0 :
        count+=1
print(count)




# n,k = map(int,input().split())
# L = map(int,input().split())
# temp = L[k-1]
# count=0
# for i in range(0,len(L)):
#     if L[i]>=temp and L[i]>0 :
#         count+=1
# print (count)