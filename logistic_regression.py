import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([0,0,0,0,1,1,1,1])

model = LogisticRegression()
model.fit(X,y)

print("Prediction for 6 hours:", model.predict([[6]])[0])
print("Accuracy:", model.score(X,y))
