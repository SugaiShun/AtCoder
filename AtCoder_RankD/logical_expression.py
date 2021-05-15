def main():
    N = int(input())
    S = [ input() for i in range(N) ]

    cnt=1
    for i in range(N):
        if S[i] == "OR":
            cnt += 1<<(i+1)
        else:
            pass
    print(cnt)

main()