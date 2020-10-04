import statsmodels.formula.api as sm
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import rasa.actions
import datetime

def linear_regression(request):

  def process_data(age, sex, bmi, children, smoker):
    if isdigits(age):
        age1 = int(age)
        if age2 > 1000:
          today = datetime.datetime.now()
          return(this.year - age1, sex, bmi, children, smoker)
        return (age1, sex, bmi, children, smoker)
    else:
      age1 = words_to_int[age]
      return (age1, sex, bmi, children, smoker)

  def predict(age, sex, bmi, children, smoker):
    return math.exp(abs(beta_0 + age * beta_1 + sex * beta_2 + bmi * beta_3 + children * beta_4 + smoker * beta_5))

# def accurarcy(u, v, w):
#   if abs(u - v) < w:
#     return True
#   else:
#     return False

  if request == POST:
    data = pd.read_csv("insurance.csv")

    data['sex_male'] = data.sex.map({'female': 0, 'male': 1})
    data['smoker_yes'] = data.smoker.map({'no': 0, 'yes': 1})
    formulated_data = pd.DataFrame({'age': data['age'][:1000], 'sex': data['sex_male'][:1000], 'bmi': data['bmi'][:1000], 'children': data['children'][:1000], 'smoker': data['smoker_yes'][:1000], 'expenses': data['expenses'][:1000]})
    test_data = pd.DataFrame({'age': data['age'][1000:], 'sex': data['sex_male'][1000:], 'bmi': data['bmi'][1000:], 'children': data['children'][1000:], 'smoker': data['smoker_yes'][1000:], 'expenses': data['expenses'][1000:]})


    sk_model = LinearRegression()
    sk_model.fit(formulated_data.drop('expenses', axis=1), formulated_data.expenses)

    # print("Intercept: ", sk_model.intercept_)
    # print("Coefficients: ", sk_model.coef_)
    #
    results = sm.ols('expenses ~ age + sex + bmi + children + smoker', formulated_data).fit()
    # print(results.summary())
    #
    # formulated_data.hist('expenses')

    formulated_data['expenses'] = np.log(formulated_data['expenses'])
    # formulated_data.hist('expenses')

    results_2 = sm.ols('expenses ~ age + sex + bmi + children + smoker', formulated_data).fit()
    # print(results_2.summary())

    words = [
          "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
          "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
          "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
        ]

    numbers = list(range(21))
    numbers.add([30, 40, 50, 60, 70, 80, 90])
    words_to_int = dict()
    for i, j in zip(words, numbers):
      words_to_int[i] = j

    beta_0, beta_1, beta_2, beta_3, beta_4, beta_5 = results_2.params
    user_data = rasa.actions.slot_mappings()
    age, sex, bmi, children, smoker = (user_data["age"], user_data["sex"], user_data["bmi"], user_data["children"], user_data["smoker"])
    return(request, predict(age, sex, bmi, children, smoker))
    # accurarcy_matrix = 0
    #
    # for index, row in test_data.iterrows():
    #   prediction = predict(row['age'], row['sex'], row['bmi'], row['children'], row['smoker'])
    #   accurarcy_matrix += accurarcy(prediction, row['expenses'], 1250)
    # print(accurarcy_matrix / test_data.shape[0])