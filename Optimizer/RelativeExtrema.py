import sympy as sp # I love this Library
import numpy as np
    
def RelativeExtrema(F, X, show=False):
    df  = [sp.diff(F, X[i]) for i in range(len(X))]
    Xm  = list(sp.nonlinsolve(df, X))
    Val = []
    for i in Xm:
        val = sp.N(F.subs([(X[j], i[j]) for j in range(len(X))]))
        if val.is_real:
            Val.append(val)
    if len(Val) == 0:
        if show == True:
            print("\n-------------------------------------------------------------------------------")
            print("\tWarning :  f{} = {} is infeasible".format(X, F))
            print("-------------------------------------------------------------------------------\n")
        return [None, None], [None, None]
    OptimalSol, OptimalVal = [Xm[np.argmin(Val)], Xm[np.argmax(Val)]], [min(Val), max(Val)]
    if show == True:
        print("f{} = {}\n".format(X, F))
        print("\tRelative Minimum point is {} with value {}".format(OptimalSol[0], OptimalVal[0]))
        print("\tRelative Maximum point is {} with value {}".format(OptimalSol[1], OptimalVal[1]))
    return OptimalSol, OptimalVal

def f():
    x, y = X = sp.symbols('x y', real=True)
    return X, (x**3 / 3 - x**2 / 2 - 12*x + (2*y+1) ** 2 + 1) ** .5

def g():
    x, y, z = X = sp.symbols('x y z', real=True)
    A = sp.exp(2.3*x + 1.4*y - 2.3*z)
    return X, A

if __name__ == '__main__':
    X, F = f()
    OptimalSol, OptimalVal = RelativeExtrema(F, X, show=True)
    
    X, F = g() 
    OptimalSol, OptimalVal = RelativeExtrema(F, X, show=True)