import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([2,4,6,8]).reshape(-1,1)
y = np.array([50,65,75,90])

model = LinearRegression()
model.fit(X,y)

print("Prediction for 7 hours:", model.predict([[7]])[0])
print("R2 Score:", model.score(X,y))
