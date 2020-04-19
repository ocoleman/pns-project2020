#Owen Coleman
#Project 2020
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def summary():
    with open('Analysis.md', 'w') as f:
        f.write("<h1>Analysis of the Dataset.</h1>")
        f.write("\n")
        f.write("\n<h2>PART I: Histogram Analysis</h2>")
        f.write("\n")
        f.write("\n")
        f.write("<h3>Petal Length</h3>")
        f.write("\n")
        f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-petal_length.png' alt='Histogram-Petal Length' align='middle'>")
        f.write("\n")
        f.write("""\nAs we can see from the histogram above, the Petal length of the Setosa flowers are tightly situated between 1 and 2 centimetres, with the majority being around the 1.5-centimetre mark.
The length of the other two species cover a much larger range, between 3 centimetres and just under 7 centimetres. 
Despite this it seems the petal length of the Iris Virginica is easily distinguishable as the largest of the 3 species of flower.""")
        f.write("\n ")
        f.write("\n <h3>Petal Width</h3>")
        f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-petal_width.png' alt='Histogram-Petal Width' align='middle'>")
        f.write("\n ")
        f.write("""\nSimilar results can be observed in each species’ petal width, with the Setosa flower being easily distinguishable as the smallest, with the majority being in the range of 0.1 to 0.5cm.
The Virginica has the largest Petal Width, despite this their width varies over a slightly broader range, measuring anywhere from just under 1.5cm to 2.5cm. """)
        f.write("\n ")
        f.write("\n <h3>Sepal Length</h3>")
        f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-sepal_length.png' alt='Histogram-Sepal Length' align='middle'>")
        f.write("\n ")

        f.write("""\nObserving now the Sepal length, we can see this is a prominently large feature of all three of the recorded Iris species.
Despite this, we can still somewhat distinguish the Sentosa’s Sepal Length as the smallest, with the vast majority of records placing their length around the 5cm mark.
The other two species cover a much broader range, with the Iris Versicolor sharing significant overlap in size with the Iris Virginica, this makes these two species harder to distinguish between.     
""")
        f.write("\n ")
        f.write("\n <h3>Sepal Width</h3>")
        f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-sepal_width.png' alt='Histogram-Sepal Width' align='middle'>")
        f.write("\n ")
        f.write("""\nFinally, we have the Sepal Width. As with the previous graph, significant overlap can be observed, however in this visualisation we can see that the Setosas appear to possess a distinguishably wide sepal as compared with the other two species.
The Versicolor and Virginica present as slightly smaller with a majority of records found in the range between 2.5 and 3.5cm. """)
        f.write("\n ")
        f.write("\n ")
        f.write("\n <h2>Summary</h2>")
        f.write("\n ")
        f.write("""\nInitial Histogram analysis suggests that the Iris setosa has the smallest features of the three species, except in the case of its sepal width, which was found to be the largest of three flowers.
The Iris versicolor and virginica were less easily distinguished across the records. However, in most cases they were larger of the two.  """)





def hist(df):

    iris_set = df[df['species'] == 'setosa']
    iris_vers = df[df['species'] == 'versicolor']
    iris_virg = df[df['species'] == 'virginica']

    plt.hist(iris_set['petal_length'], color = "red", edgecolor="white", label="Iris Setosa")
    plt.hist(iris_vers['petal_length'], color = "green", edgecolor="white", label="Iris Versicolor")
    plt.hist(iris_virg['petal_length'], color = "blue", edgecolor="white", label="Iris Virginica")
    plt.legend(loc="upper right")
    plt.title("Petal Length")
    plt.xlabel("Length(cm) >>")
    plt.ylabel("Count >>")
    plt.savefig("plots/hist-petal_length.png")
    plt.clf()


    plt.hist(iris_set['petal_width'], color = "red", edgecolor="white", label="Iris Setosa")
    plt.hist(iris_vers['petal_width'], color = "green", edgecolor="white", label="Iris Versicolor")
    plt.hist(iris_virg['petal_width'], color = "blue", edgecolor="white", label="Iris Virginica")
    plt.legend()
    plt.title("Petal Width")
    plt.xlabel("Length(cm) >>")
    plt.ylabel("Count >>")
    plt.savefig("plots/hist-petal_width.png")
    plt.clf()


    plt.hist(iris_set['sepal_length'], color = "red", edgecolor="white", label="Iris Setosa")
    plt.hist(iris_vers['sepal_length'], color = "green", edgecolor="white", label="Iris Versicolor")
    plt.hist(iris_virg['sepal_length'], color = "blue", edgecolor="white", label="Iris Virginica")
    plt.legend()
    plt.title("Sepal Length")
    plt.xlabel("Length(cm) >>")
    plt.ylabel("Count >>")
    plt.savefig("plots/hist-sepal_length.png")
    plt.clf()


    plt.hist(iris_set['sepal_width'], color = "red", edgecolor="white", label="Iris Setosa")
    plt.hist(iris_vers['sepal_width'], color = "green", edgecolor="white", label="Iris Versicolor")
    plt.hist(iris_virg['sepal_width'], color = "blue", edgecolor="white", label="Iris Virginica")
    plt.legend()
    plt.title("Sepal Width")
    plt.xlabel("Length(cm) >>")
    plt.ylabel("Count >>")
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
    plots(df)




if __name__ == "__main__":
    main()