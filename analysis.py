#Owen Coleman
#Project 2020
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#Summary function, creates a .md file that contains analysis of the investigation of this dataset. Output is formatted so that it displays neatly.
def summary():
        
        with open('Analysis.md', 'w') as f:
                f.write("\n<h1>Analysis of the Dataset.</h1>")
                f.write("\n")
                f.write("\n<h2>PART I: Histogram Analysis</h2>")
                f.write("\n")
                f.write("\n")
                f.write("\n")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-petal_length.png' alt='Histogram-Petal Length'>")
                f.write("\n</div> ")
                f.write("\n")
                f.write("""\nAs we can see from the histogram above, the Petal length of the Setosa flowers are tightly situated between 1 and 2 centimetres, with the majority being around the 1.5-centimetre mark.
The length of the other two species cover a much larger range, between 3 centimetres and just under 7 centimetres. 
Despite this it seems the petal length of the Iris Virginica is easily distinguishable as the largest of the 3 species of flower.""")
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-petal_width.png' alt='Histogram-Petal Width'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nSimilar results can be observed in each species’ petal width, with the Setosa flower being easily distinguishable as the smallest, with the majority being in the range of 0.1 to 0.5cm.
The Virginica has the largest Petal Width, despite this their width varies over a slightly broader range, measuring anywhere from just under 1.5cm to 2.5cm. """)
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-sepal_length.png' alt='Histogram-Sepal Length'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nObserving now the Sepal length, we can see this is a prominently large feature of all three of the recorded Iris species.
Despite this, we can still somewhat distinguish the Sentosa’s Sepal Length as the smallest, with the vast majority of records placing their length around the 5cm mark.
The other two species cover a much broader range, with the Iris Versicolor sharing significant overlap in size with the Iris Virginica, this makes these two species harder to distinguish between. """)
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-sepal_width.png' alt='Histogram-Sepal Width'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nFinally, we have the Sepal Width. As with the previous graph, significant overlap can be observed, however in this visualisation we can see that the Setosas appear to possess a distinguishably wide sepal as compared with the other two species.
The Versicolor and Virginica present as slightly smaller with a majority of records found in the range between 2.5 and 3.5cm. """)
                f.write("\n ")
                f.write("\n")
                f.write("\n<h2>PART II: Scatter Plot Analysis</h2>")
                f.write("\n")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/1sepallength-vs-sepalwidth.png' alt='SepalLengthvsSepalWidth'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nAs the earlier histograms showed, the Iris Setosa had a wide sepal. However, it would appear the Setosa’s sepal width is less distinguishable as previously indicated.
 From this scatter plot, significant overlap appears to exist at the upper bounds of the Versicolor and Virginica’s records, making the Setosa less reliably recognisable by this feature alone.
A natural correlation between sepal length and width can be observed in the Setosa, as length increases so too does the sepal’s width.""")
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/9petallength-vs-petalwidth.png' alt='PetalLengthvsPetalWidth'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nLooking now at how petal length compares to petal width of the three species, immediately we can see a length to width correlation. This could be classified as a strong correlation, given how tightly packed all records appear in the scatter plot.
The Setosa possesses the smallest petal Length and petal width in this dataset.
While some instances of overlap can be observed in the other two species, the Virginica is more often than not in possession of the larger Petal length and Width.""")
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/6sepalwidth-vs-petalwidth.png' alt='SepalWidthvsPetalWidth'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nResults so far have indicated the Iris Setosa is probably the smallest overall, this trend continues as we compare sepal width and petal width.
We can see the Setosa has the thinnest petal, with most being about 0.1 to 0.5 cm in length. """)
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/2sepallength-vs-petallength.png' alt='SepalLengthvsPetalLength'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nWe can see significant overlap in the length of the three species sepal. This was previous observed in the histogram data as a weak identifier of the flower’s species. 
While the Setosa may still appear smaller, there are several outliers amongst the other two species which throw off any trend identification effort. 
The other interesting thing to note is that there doesn’t seem to be any meaningful correlation between the sepal and petal length for the Setosa, despite a strong one being observable amongst the other two species. """)
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/10petalwidth-vs-sepallength.png' alt='PetalWidthvsSepalLength' >")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nIn what can be seen as a weak correlation at most, the sepal length does somewhat appear to increase as the petal widens across the three species, this trend arguably doesn’t effect the smaller Setosa in this scatter plot, who remain much more distinguishable than the other two when compared by petal width.""")
                f.write("\n ")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/8petallength-vs-sepalwidth.png' alt='PetalLengthvsSepalWidth'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\nFinally, we see the measure of petal length to sepal width, we can observe similar trends, such as the generally wider sepal of the Setosa, and the longer petal of the Virginica.
Additionally, argument could be made for the existence of a weak correlation amongst the records of the Versicolor and Virginica flowers.""")
                f.write("\n")
                f.write("\n")
                f.write("\n<h2>PART III: Summary</h2>")
                f.write("\n")
                f.write("<div align='center'>")
                f.write("\n <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/matrix.png' alt='Matrix'>")
                f.write("\n</div> ")
                f.write("\n ")
                f.write("""\n Trends that were observed amongst the histogram data were compounded by the results of the scatter plots. One such instance of this could be observed in the Iris’ sepal length, where significant overlap occurred alongside the existence of outliers among the Versicolors and Virginicas.
Conversely, initial indications implied the Setosas broad sepal would be one of the flowers key features, however further investigation showed this to be a less reliable metric for identifying the species. Despite this, the Iris Setosa time and again trended towards the left side of the axis. This leads me to conclude it is likely the smallest of the three flowers. The Virginica is probably the largest as was evident by its large features, such as possessing a longer and wider petal.
The Versicolor was found to be somewhere in the middle, although it often shared overlap with the Virginica, at times making it at times making the two indistinguishable (see Sepal Length). """)
                f.write("\n ")
                f.write("\n <h3>Below are some numerical statistics</h3>")
                f.write("\n ")

#Function that creates and saves images of the histograms of each variable.
def hist(df):
        
        #specifies each of the three species from within the dataframe, this was utilized heavily throughout this project for comparing the different variables.
        iris_set = df[df['species'] == 'setosa']
        iris_vers = df[df['species'] == 'versicolor']
        iris_virg = df[df['species'] == 'virginica']
        
        ###Petal Length###
        plt.hist(iris_set['petal_length'], color = "red", edgecolor="white", label="Iris Setosa")
        plt.hist(iris_vers['petal_length'], color = "green", edgecolor="white", label="Iris Versicolor")
        plt.hist(iris_virg['petal_length'], color = "blue", edgecolor="white", label="Iris Virginica")
        plt.legend(loc="upper right")
        plt.title("Petal Length")
        plt.xlabel("Length(cm) >>")
        plt.ylabel("Count >>")
        plt.savefig("plots/hist-petal_length.png")
        plt.clf()

        ###Petal Width###
        plt.hist(iris_set['petal_width'], color = "red", edgecolor="white", label="Iris Setosa")
        plt.hist(iris_vers['petal_width'], color = "green", edgecolor="white", label="Iris Versicolor")
        plt.hist(iris_virg['petal_width'], color = "blue", edgecolor="white", label="Iris Virginica")
        plt.legend()
        plt.title("Petal Width")
        plt.xlabel("Length(cm) >>")
        plt.ylabel("Count >>")
        plt.savefig("plots/hist-petal_width.png")
        plt.clf()

        ###Sepal Length###
        plt.hist(iris_set['sepal_length'], color = "red", edgecolor="white", label="Iris Setosa")
        plt.hist(iris_vers['sepal_length'], color = "green", edgecolor="white", label="Iris Versicolor")
        plt.hist(iris_virg['sepal_length'], color = "blue", edgecolor="white", label="Iris Virginica")
        plt.legend()
        plt.title("Sepal Length")
        plt.xlabel("Length(cm) >>")
        plt.ylabel("Count >>")
        plt.savefig("plots/hist-sepal_length.png")
        plt.clf()

        ###Sepal Width###
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
        
        #Below are the scatter plots comparing each pair of variables. In total there are 12 comparison scatter plots created by this function.

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

def matrix():
        
        #Seaborn data matrix, combining the histograms and scatter plots into 1 plot. 
        colors = ["red", "green", "blue"]
        sns.set(style="ticks")
        iris = sns.load_dataset("iris")
        g = sns.PairGrid(iris, hue="species", palette= colors)
        g.map_diag(plt.hist)
        g.map_offdiag(plt.scatter, s=5)
        g.add_legend()
        g.savefig("plots/matrix.png")

def table(df):
        #Table that outputs some of the numeric data that can be extracted by pandas. 
        iris_set = df[df['species'] == 'setosa']
        iris_vers = df[df['species'] == 'versicolor']
        iris_virg = df[df['species'] == 'virginica']

        
        #pandas.describe() functions
        seto = iris_set.describe(percentiles=[])
        vers = iris_vers.describe(percentiles=[])
        virg = iris_virg.describe(percentiles=[])

        with open('Tables.md', 'w') as f:
                f.write("<p align='center'><b>Iris Setosa Statistics </b></p>")
                f.write(seto.to_html().replace('border="1"','border="0"'))
                f.write("<p align='center'><b>Iris Versicolor Statistics </b></p>")
                f.write(vers.to_html().replace('border="1"','border="0"'))
                f.write("<p align='center'><b>Iris Virginica Statistics </b></p>")
                f.write(virg.to_html().replace('border="1"','border="0"'))
       
        with open("Tables.md") as f:
                lines = f.readlines()
                
                with open("Analysis.md", "a") as f1:
                        f1.writelines(lines)





def main():
        #main function which calls all the other functions, also contains the main 'df' variable which reads the dataset. 
        print("")
        print("Running...")
        df = pd.read_csv("iris.csv")
        summary()
        print(".")
        hist(df)
        print(".")
        plots(df)
        print(".")
        matrix()
        print(".")
        table(df)
        print("Done!")




if __name__ == "__main__":

        main()