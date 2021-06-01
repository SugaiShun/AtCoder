def check(X,A,B):
    cnt = 0
    x = X
    while 1:
        x = x*A
        if B <= x:
            x = x/A
            break
        else:
            cnt += 1

    return cnt,x

def main():
    X,Y,A,B=map(int,input().split())

    Acnt,newx = check(X,A,B)
    nokori = Y - newx
    Bcnt = int(nokori / B)
    print(Acnt+Bcnt)


if __name__=="__main__":
    main()