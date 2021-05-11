def find_divisor(n):
'''
find divisor
'''
    res = []
    i = 0
    while i*i<n:
        if n%i==0:
            res.append(i)
            res.append(n//i)
        i+=1
    return res


def main():
    return 0

main()