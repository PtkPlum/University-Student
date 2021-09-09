import sympy as sp # I love this Library
import numpy as np

def NewtonOptimizer(F, X, eps=1e-4, Alpha=1, dtype='complex', show=False):
    Xnew = np.array([1 for i in X])
    Xold = np.array([1e500 for i in X])
    n = 0
    if show:
        print("f{} = {}\n".format(X,F))
    while (np.sum((Xnew - Xold) ** 2)) ** .5 > eps:
        Sub    = [(X[i], Xnew[i]) for i in range(len(X))]
        df     = [sp.diff(F, X[i]) for i in range(len(X))]
        df     = np.array([sp.N(df[i].subs(Sub)) for i in range(len(X))], dtype=dtype)
        Xold   = Xnew
        Xnew   = Xold -  Alpha * df
        n += 1
        if show:
            print("\tX{} = {}\n".format(n,Xold))
            
    OptimalSol = Xnew
    OptimalVal = sp.N(F.subs(Sub))
    if show:
        print("---------------------------------------------------------------")
        print("\tOptimalSol =", OptimalSol)
        print("\tOptimalVal =", OptimalVal)  
        print("---------------------------------------------------------------\n\n")

    return OptimalSol, OptimalVal

def f():
    x, y = X = sp.symbols('x y', real=True)
    return X, (x**3 / 3 - x**2 / 2 - 12*x + (2*y+1) ** 2 + 1) ** .5

def g():
    x, y, z = X = sp.symbols('x y z', real=True)
    A = sp.exp(2.3*x + 1.4*y - 2.3*z)
    return X, A

def h():
    x, y = X = sp.symbols('x y', real=True)
    return X, (4 * x * y**2) + (3 * x**2 * y**4)

if __name__ == '__main__':
    X, F = f()
    OptimalSol, OptimalVal = NewtonOptimizer(F, X, dtype="complex", show=True)
    
    X, F = g()
    OptimalSol, OptimalVal = NewtonOptimizer(F, X, dtype="float", show=True)
    
    X, F = h()
    OptimalSol, OptimalVal = NewtonOptimizer(F, X, dtype="complex", show=True)
