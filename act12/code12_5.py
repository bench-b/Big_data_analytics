import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import mean_absolute_error as MAE
import matplotlib.pyplot as plt

#data preparation
df = pd.read_csv('../data/prestige.csv')
df.head()

X = df[['education', 'women', 'prestige']]
y= df[['income']]

X

#separate training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

#create a model
model=LR()
model.fit(X_train, y_train)

#check the regression equation
model.coef_
model.intercept_

#Model Evaluation: MAE
pred =model.predict(X_test)
MAE(y_test, pred)

plt.scatter(y_test, pred, color="red",)
plt.xlim([5000,16000])
plt.ylim([5000,16000])
plt.xlabel('y_test')
plt.ylabel('pred')
plt.plot(y_test,y_test, color="blue") #draw diagonal line
plt.show()

