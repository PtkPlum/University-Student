import pandas as pd
import sympy  as sp 
    
def cost(s, S):
    result = data.copy()
    
    for i in range(1, len(result)):
        # OrderNow
        result["OrderNow"][i] = 0
        if result["OrderNow"][i-1] == 0:
            if result["Inventory"][i-1] - result["Demand"][i] < s:
                result["OrderNow"][i] = 1
                
        # Inventory
        if i >= LT:
            if result["OrderNow"][i-LT] == 1:
                result["Inventory"][i] = S
            else:
                result["Inventory"][i] = max(0, result["Inventory"][i-1] - result["Demand"][i])
        else:
            result["Inventory"][i] = max(0, result["Inventory"][i-1] - result["Demand"][i])

    
    for i in range(1, len(result)):
        # OrderSize
        if i < len(result) - LT:
            result["OrderSize"][i] = max(0, result["Inventory"][i+LT] - result["Inventory"][i+LT-1])
        else:
            result["OrderSize"][i] = 0
            
        # Cost
        result["TotalOC"][i]   = result["OrderNow"][i] * OC
        result["TotalHC"][i]   = result["Inventory"][i] * HC
        result["TotalSC"][i]   = max(0, result["Demand"][i] - result["Inventory"][i-1]) * SC
        result["TotalCost"][i] = result["TotalOC"][i] + result["TotalHC"] [i] + result["TotalSC"][i]
        
        # s S
        result["s"][0] = s
        result["S"][0] = S
        
    AllTotalCost = sum(result["TotalCost"])
    return AllTotalCost, result


def GoldenSectionSearch(variable, FindS=True, a=-10000, b=10000, tol=1e-6):
    model = pd.DataFrame()
    A, B, D, X1, X2, F1, F2 = [], [], [], [], [], [], []
    GolRatio = (5 ** .5 - 1) / 2
    while b-a > tol:
        d = GolRatio * (b-a)
        x1, x2 = a+d, b-d
        if FindS == True:            
            if variable > x1:
                x1 = variable
            if variable > x2:
                x2 = variable
            f1 = cost(variable, x1)[0]
            f2 = cost(variable, x2)[0]

        else:
            if variable < x1:
                x1 = variable
            if variable < x2:
                x2 = variable
            f1 = cost(x1, variable)[0]
            f2 = cost(x2, variable)[0]
        
        if f1 > f2:
            b = x1
        else:
            a = x2
            
        print("a =",a, " b =",b)
            
        A.append(a)
        B.append(b)
        D.append(d)
        X1.append(x1)
        X2.append(x2)
        F1.append(f1)
        F2.append(f2)
        
    model["a"] = A
    model["b"] = B
    model["d"] = D
    model["x1"] = X1
    model["x2"] = X2
    model["f1"] = F1
    model["f2"] = F2
    return (a+b) / 2, (f1 + f2) / 2, model


data   = pd.read_excel("Inventory.xlsx")
Column = data.columns

Demand = data[Column[2]]
OC     = data[Column[10]][0]
HC     = data[Column[11]][0] 
SC     = data[Column[12]][0]
LT     = data[Column[13]][0]

S, value, model = GoldenSectionSearch(30, FindS=True, a=30)
simulate = cost(30, S)[1]
print(1)

writer = pd.ExcelWriter('sS-Policy_Solution.xlsx', engine='xlsxwriter')
model.to_excel(writer, index=False, sheet_name="step1")
simulate.to_excel(writer, index=False, sheet_name="simulate1")

s, value, model = GoldenSectionSearch(S, FindS=False, b=S)
simulate = cost(s, S)[1]
print(2)

model.to_excel(writer, index=False, sheet_name="step2")
simulate.to_excel(writer, index=False, sheet_name="simulate2")


S, value, model = GoldenSectionSearch(s, FindS=True, a=s)
simulate = cost(s, S)[1]
print(3)

model.to_excel(writer, index=False, sheet_name="step3")
simulate.to_excel(writer, index=False, sheet_name="simulate3")

s, value, model = GoldenSectionSearch(S, FindS=False, b=S)
simulate = cost(s, S)[1]
print(4)

model.to_excel(writer, index=False, sheet_name="step4")
simulate.to_excel(writer, index=False, sheet_name="simulate4")
writer.save()

print("\n\n--------------------------------------------------------------")
print("\tReorder point is {}".format(s))
print("\tOrder the item to {}".format(S))
print("--------------------------------------------------------------")
