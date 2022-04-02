import sys

def fib(n, x):
    x = x + 1
    if n<=1:
        print(x)
        return 1
    return fib(n-1, x) + fib(n-2, x)


n = len(sys.argv)
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     

fib(int(sys.argv[1]), int(sys.argv[2]))