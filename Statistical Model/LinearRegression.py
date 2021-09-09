import numpy as np

# Multiple Linear Regression with 2 variables and 1 target
data = np.array([[10, 50, 80, 70], 
                 [20, 60, 90, 50], 
                 [30, 80, 100, 90]])


X1 = data[0]
X2 = data[1]
Y  = data[2]
N  = len(X1)

# mean of our inputs and outputs
X1_Sum = np.sum(X1)
X2_Sum = np.sum(X2)
Y_Sum  = np.sum(Y)

X1sq_Sum = np.sum(X1 ** 2)
X2sq_Sum = np.sum(X2 ** 2)

X1X2_Sum = np.sum(X1 * X2)
X1Y_Sum  = np.sum(X1 * Y )
X2Y_Sum  = np.sum(X2 * Y)

x1sq_Sum = X1sq_Sum - (X1_Sum ** 2 / N)
x2sq_Sum = X2sq_Sum - (X2_Sum ** 2 / N)

x1x2_Sum = X1X2_Sum - X1_Sum * X2_Sum / N 
x1y_Sum  = X1Y_Sum  - X1_Sum * Y_Sum / N 
x2y_Sum  = X2Y_Sum  - X2_Sum * Y_Sum / N

b1 = (x2sq_Sum * x1y_Sum - x1x2_Sum * x2y_Sum) / (x1sq_Sum * x2sq_Sum - x1x2_Sum ** 2)
b2 = (x1sq_Sum * x2y_Sum - x1x2_Sum * x1y_Sum) / (x1sq_Sum * x2sq_Sum - x1x2_Sum ** 2)
a  = (Y_Sum - b1 * X1_Sum - b2 * X2_Sum) / N

print("a =", a)
print("b1 =", b1)
print("b2 =", b2)
