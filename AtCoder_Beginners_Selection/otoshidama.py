input_data = input()

input_data_ny = input_data.split()
N = int(input_data_ny[0])
Y = int(input_data_ny[1])

use1 = int(Y / 1000)

if use1 == N:
    print("0 0 {}".format(use1))
else:
    flag = False
    diff = use1 - N
    i_max = int(diff/4)
    j_max = int(diff/9)
    for i in range(i_max+1):
        for j in range(j_max+1):
            if i*4+j*9 == diff:
                flag = True
                break
        if flag:
            break

    if flag and (N-i-j)>=0:
        print("{0} {1} {2}".format(j,i,N-i-j))
    else:
        print("-1 -1 -1")
