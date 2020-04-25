# pns-project2020

<h2> Introduction </h2>
The Fisher's Iris data set is a multivariate data set that contains 150 records taken from three different species of iris flower. The data set was first introduced by biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*. Fisher has been called a genius and "the single most important figure in 20th century statistics". The Iris flower dataset is still used as an example of discriminant analysis, a method which is used in machine learning and pattern recognition. This is due to it being once of the first widely available datasets of its kind. For each of the three species of Iris measured in the data set, there are 50 samples, with each sample having 4 features: the sepal length and sepal width of each flower (in centimeters). 

<img src="https://thegoodpython.com/assets/images/iris-species.png" alt="Iris Species">

<p align="center">Iris flower species (Iris setosa, I. virginica and I. versicolor)</p>

<br>
<br>
<h2> Running Analysis.py </h2>

In order to run the Analysis.py python script for this project, you must have the Pandas, Matplotlib.pyplot and Seaborn libraries installed on your machine. Thankfully this all comes preinstalled with the Anaconda distribution of Python, which is also recommended. The script itself can be executed through any command terminal by simply typing "python Analysis.py" and hitting enter. The script takes 
about 5 seconds to run depending on your computer, after which point the terminal will inform you once it has finished. 


The script itself has several different functions programmed into it, these functions are in no particular order as having them be was not of concern for this project. Moving linearly through the program, the first function, summary(), creates the Analysis.md which then has the results of the analysis derived from the plots written in to it. Follwing summary, we have several functions which output histograms and scatterplots of the different species variables. These plot generation fucntions were split up primarily to reduce clutter and for ease of understanding. The plot functions utilize matplotlib.pyplot when outputting the scatter plots and histograms. Seaborn is also utilized here to produce a complete matrix of the dataset. The final function creates a table and populates it with various different pieces of numerical information relevant to the variables in the dataset. 


<h2>Current & Future Analysis of the Dataset.</h2>




<h2> Sources </h2>
https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

