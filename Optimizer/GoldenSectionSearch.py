# Minimize f(x) using line search method
import sympy as sp

def GoldenSectionSearch(F, x, a=-10000, b=10000, tol=1e-6):
    GolRatio = (5 ** .5 - 1) / 2
    while b-a > tol:
        d = GolRatio * (b-a)
        x1, x2 = a+d, b-d
        f1 = sp.N(F.subs([(x,x1)]))
        f2 = sp.N(F.subs([(x,x2)]))
        if f1 > f2:
            b = x1
        else:
            a = x2
    return (a+b) / 2, (f1 + f2) / 2


def FibonacciSearch(F, x, a=-10000, b=10000, tol=1e-6):
    fiboN = [1, 1]
    n = 1
    while (b-a)/fiboN[n] >= tol:
        fiboN.append(fiboN[n-1] + fiboN[n])
        n += 1
    x1 = a + (b-a) * fiboN[n-2] / fiboN[n]
    x2 = a + (b-a) * fiboN[n-1] / fiboN[n]
    f1 = sp.N(F.subs([(x,x1)]))
    f2 = sp.N(F.subs([(x,x2)]))
    while n != 2:
        n -= 1
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = a + (b-a) * fiboN[n-2] / fiboN[n]
            f1 = sp.N(F.subs([(x,x1)]))
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + (b-a) * fiboN[n-1] / fiboN[n]
            f2 = sp.N(F.subs([(x,x2)]))
    return (a+b) / 2, (f1+f2)/2


def AllMethod(F, X):
    print("\nMinimize function f({}) = {}\n".format(X, F))

    sol, value = GoldenSectionSearch(F, X, tol=1e-12)
    print("\tFor Golden Section Search")
    print("\t\tThe optimal solution is", sol, "\n\t\twith the minimum value", value, "\n")

    sol, value = FibonacciSearch(F, X, tol=1e-12)
    print("\tFor Fibonacci Search")
    print("\t\tthe optimal solution is", sol, "\n\t\twith the minimum value", value, "\n")
    
    print("---------------------------------------------------------------")

def f():  # Objective of this program is any function can be inputted
    x = sp.Symbol('x')
    return [x], (x - 4) ** 2

def g():
    x = sp.Symbol('x')
    return [x], sp.sin(x*sp.pi) ** 2 - x**(-3)
    
if __name__ == '__main__':
    AllMethod(f()[1], f()[0][0])
    AllMethod(g()[1], g()[0][0])
