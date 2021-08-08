def fib(n):
    if n== 0 or n==1:
        return n
    else:
        print(fib(n-1), fib(n-2), "here")
        return fib(n-1)+ fib(n-2)

print(fib(16))