from sklearn import linear_model
import numpy as np

data = np.array([[10, 50, 80, 70],   # X1
                 [20, 60, 90, 50],   # X2
                 [0, 1, 0, 1]])      # Y

Y = data[-1]
X = data[:-1].transpose()

reg    = linear_model.LogisticRegression()
regfit = reg.fit(X, Y)

print("a  =", regfit.intercept_[0])
for i in range(len(data)-1):
    print("b{} = {}".format(i, regfit.coef_[0][i]))