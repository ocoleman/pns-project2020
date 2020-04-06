#Owen Coleman
#Project 2020
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def summary():
    with open('Analysis.txt', 'a') as f:
        f.write("TEXT GOES HERE")


def hist(df):

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

def plots(df):
    setosa = df[df['species'] == 'setosa']
    versicolor = df[df['species'] == 'versicolor']
    virginica = df[df['species'] == 'virginica']

    #compare goes here
    





def main():
    df = pd.read_csv("iris.csv")
    summary()
    hist(df)
    plots(df)




if __name__ == "__main__":
    main()