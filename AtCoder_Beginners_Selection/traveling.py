N = int(input())
plan =  [list(map(int, input().split())) for i in range(N)]

plan.insert(0,[0,0,0])
flag = True
for i in range(1,N):
    dx = abs(plan[i][1] - plan[i-1][1])
    dy = abs(plan[i][2] - plan[i-1][2])
    dt = plan[i][0] - plan[i-1][0]

    f = dt - (dx + dy)
    if f < 0 or f%2!=0: flag = False
    
if flag:
    print('Yes')
else:
    print('No')
