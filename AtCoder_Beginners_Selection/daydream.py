
T = ['dream','dreamer','erase','eraser']

S = input()
# import random
# S = ''
# for i in range(1000):
#     index = random.randint(0,3)
#     S += T[index]

def daydream(s):
    min_T_len = len('dream')
    new_S = s
    while True:

        s_len = len(new_S)
        if s_len < min_T_len:
            break

        tmp = 0
        for t in T:
            t_len = len(t)
            if new_S[-t_len:] == t:
                tmp = new_S[:-t_len]
        
        if tmp == 0:
            break
        else:
            new_S = tmp

    if new_S=='':
        print('YES')
    else:
        print('NO')

# 以下は再帰でチャレンジ
# メモリが問題の条件に一致しないため採用しなかったが解けるは解ける

# def match_T(s,t):
#     t_len = len(t)
#     s_len = len(s)
#     if s_len >= t_len and s[:t_len] == t:
#         return s[t_len:],True
#     else:
#         return s,False

# def daydream_rec(s):
#     match_s1, flg1 = match_T(s,T[0])
#     match_s2, flg2 = match_T(s,T[1])
#     match_s3, flg3 = match_T(s,T[2])
#     match_s4, flg4 = match_T(s,T[3])

#     if len(match_s1)==0 or len(match_s2)==0 or len(match_s3)==0 or len(match_s4)==0:
#         return True
#     else:

#         flg_t1 = daydream_rec(match_s1) if flg1 else False
#         flg_t2 = daydream_rec(match_s2) if flg2 else False
#         flg_t3 = daydream_rec(match_s3) if flg3 else False
#         flg_t4 = daydream_rec(match_s4) if flg4 else False

#         if any([flg_t1,flg_t2,flg_t3,flg_t4]):
#             return True
#         else:
#             return False

# import sys
# sys.setrecursionlimit(10000) # pythonの再帰の上限は標準1000くらいだからこれを上限緩和

# if daydream_rec(S):
#     print('YES')
# else:
#     print('NO')

