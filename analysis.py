#Owen Coleman
#Project 2020
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def summary():
    with open('Analysis.md', 'w') as f:
        f.write("Analysis of the Dataset.")
        f.write("\n")
        f.write("\nPART I: Histogram Analysis")
        f.write("\n")
        f.write("\nPetal Length")
        f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-petal_length.png' alt='Histogram-Petal Length'>")
        f.write("""\nAs we can see from the histogram above, the Petal length of the Setosa flowers are tightly situated between 1 and 2 centimetres, with the majority being around the 1.5-centimetre mark.
The length of the other two species cover a much larger range, between 3 centimetres and just under 7 centimetres. 
Despite this it seems the petal length of the Iris Virginica is easily distinguishable as the largest of the 3 species of flower.""")
        f.write("\n ")
        f.write("\n ")




def hist(df):

    iris_set = df[df['species'] == 'setosa']
    iris_vers = df[df['species'] == 'versicolor']
    iris_virg = df[df['species'] == 'virginica']

    plt.hist(iris_set['petal_length'], color = "skyblue", label="Iris Setosa")
    plt.hist(iris_vers['petal_length'], color = "dodgerblue", label="Iris Versicolor")
    plt.hist(iris_virg['petal_length'], color = "darkblue", label="Iris Virginica")
    plt.legend(loc="upper right")
    plt.title("Petal Length")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-petal_length.png")
    plt.clf()


    plt.hist(iris_set['petal_width'], color = "skyblue", label="Iris Setosa")
    plt.hist(iris_vers['petal_width'], color = "dodgerblue", label="Iris Versicolor")
    plt.hist(iris_virg['petal_width'], color = "darkblue", label="Iris Virginica")
    plt.legend()
    plt.title("Petal Width")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-petal_width.png")
    plt.clf()


    plt.hist(iris_set['sepal_length'], color = "skyblue", label="Iris Setosa")
    plt.hist(iris_vers['sepal_length'], color = "dodgerblue", label="Iris Versicolor")
    plt.hist(iris_virg['sepal_length'], color = "darkblue", label="Iris Virginica")
    plt.legend()
    plt.title("Sepal Length")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-sepal_length.png")
    plt.clf()


    plt.hist(iris_set['sepal_width'], color = "skyblue", label="Iris Setosa")
    plt.hist(iris_vers['sepal_width'], color = "dodgerblue", label="Iris Versicolor")
    plt.hist(iris_virg['sepal_width'], color = "darkblue", label="Iris Virginica")
    plt.legend()
    plt.title("Sepal Width")
    plt.xlabel("Length(cm) -->")
    plt.ylabel("Count -->")
    plt.savefig("plots/hist-sepal_width.png")
    plt.clf()

def plots(df):
    #Assigned variables to the data of the three species. 
    iris_set = df[df['species'] == 'setosa']
    iris_vers = df[df['species'] == 'versicolor']
    iris_virg = df[df['species'] == 'virginica']

    #####Sepal Length#####
    #---Sepal Length vs Sepal Width---
    plt.plot(iris_set["sepal_length"], iris_set["sepal_width"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["sepal_length"], iris_vers["sepal_width"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["sepal_length"], iris_virg["sepal_width"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Sepal Length vs Sepal Width (in cm)")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    #Saving and clearing the figure.
    plt.savefig("plots/1sepallength-vs-sepalwidth.png")
    plt.clf()

    #---Sepal Length vs Petal Length---
    plt.plot(iris_set["sepal_length"], iris_set["petal_length"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["sepal_length"], iris_vers["petal_length"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["sepal_length"], iris_virg["petal_length"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Sepal Length vs Petal Length (in cm)")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Length")
    #Saving and clearing the figure.
    plt.savefig("plots/2sepallength-vs-petallength.png")
    plt.clf()

    #---Sepal Length vs Petal Width---
    plt.plot(iris_set["sepal_length"], iris_set["petal_width"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["sepal_length"], iris_vers["petal_width"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["sepal_length"], iris_virg["petal_width"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Sepal Length vs Petal Width (in cm)")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Width")
    #Saving and clearing the figure.
    plt.savefig("plots/3sepallength-vs-petalwidth.png")
    plt.clf()

    #####Sepal Width#####
    #---Sepal Width vs Sepal Length---
    plt.plot(iris_set["sepal_width"], iris_set["sepal_length"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["sepal_width"], iris_vers["sepal_length"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["sepal_width"], iris_virg["sepal_length"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Sepal Width vs Sepal Length (in cm)")
    plt.xlabel("Sepal Width")
    plt.ylabel("Sepal Length")
    #Saving and clearing the figure.
    plt.savefig("plots/4sepalwidth-vs-sepallength.png")
    plt.clf()

    #---Sepal Width vs Petal Length---
    plt.plot(iris_set["sepal_width"], iris_set["petal_length"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["sepal_width"], iris_vers["petal_length"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["sepal_width"], iris_virg["petal_length"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Sepal Width vs Petal Length (in cm)")
    plt.xlabel("Sepal Width")
    plt.ylabel("Petal Length")
    #Saving and clearing the figure.
    plt.savefig("plots/5sepallwidth-vs-petallength.png")
    plt.clf()

    #---Sepal Width vs Petal Width---
    plt.plot(iris_set["sepal_width"], iris_set["petal_width"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["sepal_width"], iris_vers["petal_width"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["sepal_width"], iris_virg["petal_width"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Sepal Width vs Petal Width (in cm)")
    plt.xlabel("Sepal Width")
    plt.ylabel("Petal Width")
    #Saving and clearing the figure.
    plt.savefig("plots/6sepalwidth-vs-petalwidth.png")
    plt.clf()

    
    #####Petal Length#####
    #---Petal Length vs Sepal Length---
    plt.plot(iris_set["petal_length"], iris_set["sepal_length"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["petal_length"], iris_vers["sepal_length"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["petal_length"], iris_virg["sepal_length"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Petal Length vs Sepal Length (in cm)")
    plt.xlabel("Petal Length")
    plt.ylabel("Sepal Length")
    #Saving and clearing the figure.
    plt.savefig("plots/7petallength-vs-sepallength.png")
    plt.clf()

    #---Petal Length vs Sepal Width---
    plt.plot(iris_set["petal_length"], iris_set["sepal_width"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["petal_length"], iris_vers["sepal_width"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["petal_length"], iris_virg["sepal_width"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Petal Length vs Sepal Width (in cm)")
    plt.xlabel("Petal Length")
    plt.ylabel("Sepal Width")
    #Saving and clearing the figure.
    plt.savefig("plots/8petallength-vs-sepalwidth.png")
    plt.clf()

    #---Petal Length vs Petal Width---
    plt.plot(iris_set["petal_length"], iris_set["petal_width"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["petal_length"], iris_vers["petal_width"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["petal_length"], iris_virg["petal_width"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Petal Length vs Petal Width (in cm)")
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")
    #Saving and clearing the figure.
    plt.savefig("plots/9petallength-vs-petalwidth.png")
    plt.clf()



    #####Petal Width#####
    #---Petal Width vs Sepal Length---
    plt.plot(iris_set["petal_width"], iris_set["sepal_length"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["petal_width"], iris_vers["sepal_length"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["petal_width"], iris_virg["sepal_length"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Petal Width vs Sepal Length (in cm)")
    plt.xlabel("Petal Width")
    plt.ylabel("Sepal Length")
    #Saving and clearing the figure.
    plt.savefig("plots/10petalwidth-vs-sepallength.png")
    plt.clf()

    #---Petal Width vs Sepal width---
    plt.plot(iris_set["petal_width"], iris_set["sepal_width"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["petal_width"], iris_vers["sepal_width"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["petal_width"], iris_virg["sepal_width"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Petal Width vs Sepal Width (in cm)")
    plt.xlabel("Petal Width")
    plt.ylabel("Sepal Width")
    #Saving and clearing the figure.
    plt.savefig("plots/11petalwidth-vs-sepalwidth.png")
    plt.clf()

    #---Petal Width vs Petal Length---
    plt.plot(iris_set["petal_width"], iris_set["petal_length"], "r.", label="Iris Setosa")
    plt.plot(iris_vers["petal_width"], iris_vers["petal_length"], "g.", label="Iris Versicolor")
    plt.plot(iris_virg["petal_width"], iris_virg["petal_length"], "b.", label="Iris Virginica")
    #Providing plots with labels and a legend.
    plt.legend()
    plt.title("Petal Width vs Petal Length (in cm)")
    plt.xlabel("Petal Width")
    plt.ylabel("Petal Length")
    #Saving and clearing the figure.
    plt.savefig("plots/12petalwidth-vs-petallength.png")
    plt.clf()




def main():
    df = pd.read_csv("iris.csv")
    summary()
    hist(df)
    #plots(df)




if __name__ == "__main__":
    main()