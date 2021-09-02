from sklearn.linear_model import LinearRegression
import numpy as np

data = np.array([[10, 50, 80, 70],   # X1
                 [20, 60, 90, 50],   # X2
                 [30, 80, 100, 90]]) # Y

Y = data[-1]
X = data[:-1].transpose()

reg = LinearRegression().fit(X,Y)
for i in range(len(data)-1):
    print("b{} = {}".format(i, reg.coef_[i]))
print("a  =", reg.intercept_)
