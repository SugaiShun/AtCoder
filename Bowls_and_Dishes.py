def check_condition(CD):
    condi_cnt = 0
    for i in range(M):
        if CD[A[i]] > 0 and CD[B[i]]:
            condi_cnt+=1
    return condi_cnt

def tree_search(cd,depth,CD):
    dish = D[depth] if cd else C[depth]
    CD.append(dish)
    depth+=1
    if depth == (K-1):
        return check_condition(CD)
    return max(tree_search(0,depth,CD),tree_search(1,depth,CD))

N,M = map(int,input().split())
A = [0]*M
B = [0]*M
for i in range(M):
    A[i],B[i] = map(int,input().split())
K = int(input())
C = [0]*K
D = [0]*K
for i in range(K):
    C[i],D[i] = map(int,input().split())

CD = []
max_cnt = max(tree_search(0,0,CD),tree_search(1,0,CD))
print(max_cnt)