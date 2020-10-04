import statsmodels.formula.api as sm
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math

def predict(age, sex, bmi, children, smoker):
  return math.exp(abs(beta_0 + age * beta_1 + sex * beta_2 + bmi * beta_3 + children * beta_4 + smoker * beta_5))

def accurarcy(u, v, w):
  if abs(u - v) < w:
    return True
  else:
    return False


data = pd.read_csv("insurance.csv")
data.head()

data['sex_male'] = data.sex.map({'female': 0, 'male': 1})
data['smoker_yes'] = data.smoker.map({'no': 0, 'yes': 1})
formulated_data = pd.DataFrame({'age': data['age'][:1000], 'sex': data['sex_male'][:1000], 'bmi': data['bmi'][:1000], 'children': data['children'][:1000], 'smoker': data['smoker_yes'][:1000], 'expenses': data['expenses'][:1000]})
test_data = pd.DataFrame({'age': data['age'][1000:], 'sex': data['sex_male'][1000:], 'bmi': data['bmi'][1000:], 'children': data['children'][1000:], 'smoker': data['smoker_yes'][1000:], 'expenses': data['expenses'][1000:]})


sk_model = LinearRegression()
sk_model.fit(formulated_data.drop('expenses', axis=1), formulated_data.expenses)

print("Intercept: ", sk_model.intercept_)
print("Coefficients: ", sk_model.coef_)

results = sm.ols('expenses ~ age + sex + bmi + children + smoker', formulated_data).fit()
print(results.summary())

formulated_data.hist('expenses')

formulated_data['expenses'] = np.log(formulated_data['expenses'])
formulated_data.hist('expenses')

results_2 = sm.ols('expenses ~ age + sex + bmi + children + smoker', formulated_data).fit()
print(results_2.summary())

beta_0, beta_1, beta_2, beta_3, beta_4, beta_5 = results_2.params

accurarcy_matrix = 0

for index, row in test_data.iterrows():
  prediction = predict(row['age'], row['sex'], row['bmi'], row['children'], row['smoker'])
  accurarcy_matrix += accurarcy(prediction, row['expenses'], 1250)
print(accurarcy_matrix / test_data.shape[0])