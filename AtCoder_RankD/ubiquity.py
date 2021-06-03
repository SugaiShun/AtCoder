def main():
    N = int(input())
    out = ((9**(N-2))*(2**N-2))%(10**9+7)
    # out = (9**(N-2))*(2**N-2)
    print(out)


if __name__=="__main__":
    main()
