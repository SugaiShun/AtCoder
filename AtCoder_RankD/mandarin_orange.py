
N = int(input())
oranges = list(map(int,input().split()))

def orange_sum(a,b,x):
    return (b-a+1)*x

sort_list = sorted(set(oranges))

area_sum = 0
for i in range(len(sort_list)):
    x = sort_list[i]

    flg = 0
    start = 0
    end = N-1
    for j in range(N):
        if oranges[j] >= x and not(flg):
            start = j
            flg = 1
        elif oranges[j] < x and flg:
            end = j-1
            new_area_sum = orange_sum(start,end,x)
            if area_sum < new_area_sum:
                area_sum = new_area_sum
            flg = 0
        else:
            pass
    
    if flg:
        end = j
        new_area_sum = orange_sum(start,end,x)
        if area_sum < new_area_sum:
            area_sum = new_area_sum


print(area_sum)


