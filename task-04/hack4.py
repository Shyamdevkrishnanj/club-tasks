        
n = int(input().strip())
height = map(int,input().strip().split(' '))

cnt = 0
running_top = 0
for candle in height:
    if (candle > running_top):
        cnt = 1
        running_top = candle
    elif candle == running_top:
        cnt += 1
        
print (cnt)