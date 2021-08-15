# Minimize f(x) using line search method
def f(x):
    return (x - 4) ** 2

def GoldenSectionSearch(a=-10000, b=10000, tol=1e-6):
    GolRatio = (5 ** .5 - 1) / 2
    while b-a > tol:
        d = GolRatio * (b-a)
        x1, x2 = a+d, b-d
        if f(x1) > f(x2):
            b = x1
        else:
            a = x2
    return (a+b) / 2, (f(x1) + f(x2)) / 2


def FibonacciSearch(a=-10000, b=10000, tol=1e-6):
    fiboN = [1, 1]
    n = 1
    while (b-a)/fiboN[n] >= tol:
        fiboN.append(fiboN[n-1] + fiboN[n])
        n += 1
    x1 = a + (b-a) * fiboN[n-2] / fiboN[n]
    x2 = a + (b-a) * fiboN[n-1] / fiboN[n]
    f1 = f(x1)
    f2 = f(x2)
    while n != 2:
        n -= 1
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = a + (b-a) * fiboN[n-2] / fiboN[n]
            f1 = f(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + (b-a) * fiboN[n-1] / fiboN[n]
            f2 = f(x2)
    return (a+b) / 2, (f1+f2)/2
        
sol, value = GoldenSectionSearch(tol=1e-12)
print("For Golden Section Search\n\tThe optimal solution is", sol, "\n\twith the minimum value", value, "\n")

sol, value = FibonacciSearch(tol=1e-12)
print("For Fibonacci Search\n\tthe optimal solution is", sol, "\n\twith the minimum value", value, "\n")