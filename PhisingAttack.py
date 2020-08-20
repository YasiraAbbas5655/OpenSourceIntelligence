import collections as co
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

df = pd.read_excel('personsData.xls')

X = df[['ContactCount','Email','SocialMediaCount','SocialMediaActivityStatus','JobPlacementHistory']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['PhisingAttack']

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# prediction with sklearn

print('Predicted Vulnerability Score: \n', regr.predict([[1,1,2,2,4]]))

# with statsmodels
X = sm.add_constant(X)  # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)


