def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

a=factorial(5)
print("Result of factorial",a)
