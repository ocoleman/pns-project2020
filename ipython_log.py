# IPython log file

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('logstart', '')
df pd.read_csv("iris.csv")
df = pd.read_csv("iris.csv")
df
df["species"]
iris_set = df[df["species"] == "setosa"]
irs_set
iris_set
iris_set["sepal_length"]
plt.plot(iris_set["sepal_length"], iris_set["sepal_width"], "b.")
plt.plot(iris_set["sepal_length"], iris_set["sepal_width"], "r.")
plt.plot(iris_set["sepal_length"], iris_set["sepal_width"], "r." label="Setosa")
plt.plot(iris_set["sepal_length"], iris_set["sepal_width"], "r.", label="Setosa")
plt.legend()
plt.plot(iris_set["sepal_length"], iris_set["sepal_width"], "r.", label="Setosa")
iris_set["sepal_length"]
iris_set["sepal_width"]
df
plt.plot(iris_set["petal_length"], iris_set["petal_width"], "r.", label="Iris Setosa")
iris_vers = df[df['species'] == 'versicolor']
iris_virg = df[df['species'] == 'virginica']
plt.plot(iris_set["petal_length"], iris_set["petal_width"], "r.", label="Iris Setosa")
plt.plot(iris_vers["petal_length"], iris_set["petal_width"], "g.", label="Iris Versicolor")
exit()
