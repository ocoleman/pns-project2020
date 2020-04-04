#Owen Coleman
#Project 2020
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def summary():
    with open('Analysis.txt', 'a') as f:
        f.write("TEXT GOES HERE")


def plots():
    df = pd.read_csv("iris.csv")


    plt.hist(df['petal_length'])
    plt.title("Petal Length")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-petal_length.png")
    plt.clf()


    plt.hist(df['petal_width'])
    plt.title("Petal Width")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-petal_width.png")
    plt.clf()


    plt.hist(df['sepal_length'])
    plt.title("Sepal Length")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-sepal_length.png")
    plt.clf()


    plt.hist(df['sepal_width'])
    plt.title("Sepal Length")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-sepal_width.png")
    plt.clf()



def main():
    summary()
    plots()




if __name__ == "__main__":
    main()