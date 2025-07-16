import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('student_scores.csv')
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = LinearRegression()
model.fit(X, y)

__all__ = ['model']
