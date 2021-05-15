def check_condition(dishes):
    condi_cnt = 0
    for i in range(M):
        if dishes[A[i]] > 0 and dishes[B[i]] > 0:
            condi_cnt+=1
    return condi_cnt

def tree_search(cd,depth,CD):
    dish = D[depth] if cd else C[depth]

    CD[dish]+=1
    if depth == (K-1):
        return check_condition(CD)
    depth+=1

    return max(tree_search(0,depth,CD.copy()),tree_search(1,depth,CD.copy()))

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

CD1 = [0]*(N+1)
CD2 = [0]*(N+1)
max_cnt = max(tree_search(0,0,CD1),tree_search(1,0,CD2))
print(max_cnt)

# itertoolsを使った全探索のやり方
# from itertools import product
# pattern = list(product([0, 1], repeat=K))#2^3通り
# max_cnt = 0
# for i in range(len(pattern)):
#     dishes = [0]*(N+1)
#     for j in range(K):
#         dish = D[j] if pattern[i][j] else C[j]
#         dishes[dish]+=1
#     tmp_cnt = check_condition(dishes)
#     if max_cnt < tmp_cnt: max_cnt = tmp_cnt
# print(max_cnt)