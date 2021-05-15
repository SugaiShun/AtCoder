import sys

def main():
    N = int(input())
    read_sys = sys.stdin.readline
    A = list(map(int,read_sys().split()))

    cnt_list = [0]*200
    for i in range(N):
        cnt_list[ A[i]%200 ]+=1
    
    cnt = 0
    for i in range(200):
        c = cnt_list[i]
        cnt += c*(c-1)/2
    
    print(int(cnt))
    
    # watched = [0]*N
    # true_list = [ [] for i in range(N) ]

    # cnt = 0
    # for i in range(N):
    #     if A[i] in watched:
    #         pre_i = watched.index(A[i])
    #         if len(true_list[pre_i]) > 0:
    #             true_i = true_list[pre_i].index(A[i])
    #             true_cnt = len(true_list[pre_i]) - (true_i+1)
    #             cnt += true_cnt
    #             true_list[pre_i].pop(true_i)
    #         else:
    #             continue        
    #     else:
    #         for j in range(i+1,N):
    #             if (A[i] - A[j])%200 == 0:
    #                 cnt+=1
    #                 true_list[i].append(A[j])

    #     watched[i] = A[i]

    # print(cnt)

main()