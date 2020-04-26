# pns-project2020

<h2> Introduction </h2>
<p>The Fisher's Iris data set is a multivariate data set that contains 150 records taken from three different species of iris flower. The data set was first introduced by biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*. Fisher has been called a genius and "the single most important figure in 20th century statistics"[1]. The Iris flower dataset is still used as an example of discriminant analysis, a method which is used in machine learning and pattern recognition[2]. This is due to it being once of the first widely available datasets of its kind. For each of the three species of Iris measured in the data set, there are 50 samples, with each sample having 4 features: the sepal length and sepal width of each flower (in centimeters). </p>

<img src="https://thegoodpython.com/assets/images/iris-species.png" alt="Iris Species">

<p align="center">Iris flower species (Iris setosa, I. virginica and I. versicolor)</p>

<br>
<br>
<h2> Running Analysis.py </h2>

<p>In order to run the Analysis.py python script for this project, you must have the Pandas, Matplotlib.pyplot and Seaborn libraries installed on your machine. Thankfully this all comes preinstalled with the Anaconda distribution of Python, which is also recommended. The script itself can be executed through any command terminal by simply typing "python Analysis.py" and hitting enter. The script takes 
about 5 seconds to run depending on your computer, after which point the terminal will inform you once it has finished. </p>


<p>The script itself has several different functions programmed into it, these functions are in no particular order as having them be was not of concern for this project. Moving linearly through the program, the first function, summary(), creates the 'Analysis.md'file which then has the results of the analysis derived from the plots written in to it. Follwing summary, we have several functions which output histograms and scatterplots of the different species variables. These plot generation fucntions were split up primarily to reduce clutter and for ease of understanding. The plot functions utilize matplotlib.pyplot when outputting the scatter plots and histograms. Seaborn is also utilized here to produce a complete matrix of the dataset. The final function creates 3 tables and populates them with various different pieces of numerical information relevant to the variables in the dataset. </p>


<h2>Current & Future Analysis of the Dataset.</h2>
<p> Due to the Iris flower dataset's simplistic nature, it is an attractive model for machine learning projects. While doing research for my own project, I came across several projects that make use of the Python scikit-learn library with the overall goal of creating a model that could easily distinguish between the 3 flower species[3][4]. There were other projects that, in a similar scope to my own sought to perform a general analysis on the visualisations they could derive from the dataset[5][6]. These projects were helpful in providing me with ideas on ways to improve my own work. I also found a paper titled 'Statistical Analysis of the Iris Flower Dataset' incorporated significant numerical analysis elements such as functions to find mean, mode, median, standard deviation etc. I found this interesting and although somewhat beyond the scope of my project I decided to use certain features of pandas to produce some statistical data derived from the dataset. Overall the Iris Dataset is still a particularly popular one, I have heard it being dubbed as the "Hello World" of datasets as it is commonly used at entry level undertakings. I believe there is still much more data to be extrapolated from this dataset through the use of the many freely available Python libraries that exist. If I were to revisit this project in the future, I would like to explore the Seaborn and NumPy libraries more as I feel the data visualisation capabilities of these libraries are immense.</p>


<h2> Sources </h2>

[1] Bradley Efron, R. A. Fisher in the 21st Century, (1996), Statistical Science
1998, Vol. 13, No. 2, p. 113
<br><br>
[2] THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS, https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x
<br><br>
[3] Machine Learning with Iris Dataset, https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
<br><br>
[4] Flower Classifcation Iris Dataset, https://github.com/Kailash7dev/Flower-Classification-Iris-Dataset
<br><br>
[5] Project2018-iris, https://github.com/RitRa/Project2018-iris
<br><br>
[6] Iris Flower Data Set Project, https://github.com/ildaro/Iris-Flower
<br><br>
[7] Statistical Analysis of the Iris Flower Dataset, http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf
<br><br>

Iris Flower Dataset acquired from: https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

