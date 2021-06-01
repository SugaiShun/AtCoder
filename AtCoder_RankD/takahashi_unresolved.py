def check(X,Y,A,B):
    cnt = 0
    x = X
    while 1:
        if (X+B) <= x*A or x*A > Y:
            break
        else:
            x = x*A
            cnt += 1

    return cnt,x

def main():
    X,Y,A,B=map(int,input().split())

    Acnt,newx = check(X,Y,A,B)
    nokori = Y - newx
    Bcnt = (nokori-1) // B
    print(Acnt+Bcnt)


if __name__=="__main__":
    main()