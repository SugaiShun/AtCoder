def find_divisor(n):
    '''
    find divisor
    '''
    res = []
    i = 1
    while i*i<n:
        if n%i==0:
            res.append(i)
            res.append(n//i)
        i+=1
    return res


def main():
    N = int(input())

    divs = find_divisor(2*N)
    ans = 0
    for div in divs:
        m = (2*N)//div
        if (div-m)%2 == 1:
            ans+=1
    
    print(ans)

main()