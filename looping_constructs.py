for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
                print(n, 'equals', x, '*', n//x)
                # print("break")
                break
                # print("didnt break")
        else:
            print(n," is a prime number")

