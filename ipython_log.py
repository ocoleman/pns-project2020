# IPython log file

get_ipython().run_line_magic('logstart', '')
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")
df
plt.hist(df['petal_length'])     plt.legend()     plt.title("Petal Length")     plt.xlabel("Length -->")     plt.ylabel("Count -->")
plt.hist(df['petal_length'])
plt.legend()
plt.legend()
df.hist()

