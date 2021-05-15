def count_number(num):
    counter = [0]*10
    counter[int(num/1000)] += 1
    num1 = num - int(num/1000)*1000
    counter[int(num1/100)] += 1
    num2 = num1 - int(num1/100)*100
    counter[int(num2/10)] += 1
    num3 = num2 - int(num2/10)*10
    counter[int(num3)] += 1
    return counter

def main():
    S = input()

    cnt=0

    if S.count('o') > 4:
        print(0)
        return False


    for i in range(10000):
        counter = count_number(i)
        match = True
        for j in range(len(S)):
            if S[j]=='o' and counter[j]==0:
                match = False
            if S[j]=='x' and counter[j]>0:
                match = False
        if match:
            cnt+=1
    
        
    print(cnt)
    return True

main()


