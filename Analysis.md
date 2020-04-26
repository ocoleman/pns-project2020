
<h1>Analysis of the Dataset.</h1>

<h2>PART I: Histogram Analysis</h2>


<div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-petal_length.png' alt='Histogram-Petal Length'>
</div> 

As we can see from the histogram above, the Petal length of the Setosa flowers are tightly situated between 1 and 2 centimetres, with the majority being around the 1.5-centimetre mark.
The length of the other two species cover a much larger range, between 3 centimetres and just under 7 centimetres. 
Despite this it seems the petal length of the Iris Virginica is easily distinguishable as the largest of the 3 species of flower.
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-petal_width.png' alt='Histogram-Petal Width'>
</div> 
 
Similar results can be observed in each species’ petal width, with the Setosa flower being easily distinguishable as the smallest, with the majority being in the range of 0.1 to 0.5cm.
The Virginica has the largest Petal Width, despite this their width varies over a slightly broader range, measuring anywhere from just under 1.5cm to 2.5cm. 
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-sepal_length.png' alt='Histogram-Sepal Length'>
</div> 
 
Observing now the Sepal length, we can see this is a prominently large feature of all three of the recorded Iris species.
Despite this, we can still somewhat distinguish the Sentosa’s Sepal Length as the smallest, with the vast majority of records placing their length around the 5cm mark.
The other two species cover a much broader range, with the Iris Versicolor sharing significant overlap in size with the Iris Virginica, this makes these two species harder to distinguish between. 
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/hist-sepal_width.png' alt='Histogram-Sepal Width'>
</div> 
 
Finally, we have the Sepal Width. As with the previous graph, significant overlap can be observed, however in this visualisation we can see that the Setosas appear to possess a distinguishably wide sepal as compared with the other two species.
The Versicolor and Virginica present as slightly smaller with a majority of records found in the range between 2.5 and 3.5cm. 
 

<h2>PART II: Scatter Plot Analysis</h2>
<div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/1sepallength-vs-sepalwidth.png' alt='SepalLengthvsSepalWidth'>
</div> 
 
As the earlier histograms showed, the Iris Setosa had a wide sepal. However, it would appear the Setosa’s sepal width is less distinguishable as previously indicated.
 From this scatter plot, significant overlap appears to exist at the upper bounds of the Versicolor and Virginica’s records, making the Setosa less reliably recognisable by this feature alone.
A natural correlation between sepal length and width can be observed in the Setosa, as length increases so too does the sepal’s width.
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/9petallength-vs-petalwidth.png' alt='PetalLengthvsPetalWidth'>
</div> 
 
Looking now at how petal length compares to petal width of the three species, immediately we can see a length to width correlation. This could be classified as a strong correlation, given how tightly packed all records appear in the scatter plot.
The Setosa possesses the smallest petal Length and petal width in this dataset.
While some instances of overlap can be observed in the other two species, the Virginica is more often than not in possession of the larger Petal length and Width.
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/6sepalwidth-vs-petalwidth.png' alt='SepalWidthvsPetalWidth'>
</div> 
 
Results so far have indicated the Iris Setosa is probably the smallest overall, this trend continues as we compare sepal width and petal width.
We can see the Setosa has the thinnest petal, with most being about 0.1 to 0.5 cm in length. 
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/2sepallength-vs-petallength.png' alt='SepalLengthvsPetalLength'>
</div> 
 
We can see significant overlap in the length of the three species sepal. This was previous observed in the histogram data as a weak identifier of the flower’s species. 
While the Setosa may still appear smaller, there are several outliers amongst the other two species which throw off any trend identification effort. 
The other interesting thing to note is that there doesn’t seem to be any meaningful correlation between the sepal and petal length for the Setosa, despite a strong one being observable amongst the other two species. 
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/10petalwidth-vs-sepallength.png' alt='PetalWidthvsSepalLength' >
</div> 
 
In what can be seen as a weak correlation at most, the sepal length does somewhat appear to increase as the petal widens across the three species, this trend arguably doesn’t effect the smaller Setosa in this scatter plot, who remain much more distinguishable than the other two when compared by petal width.
 <div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/8petallength-vs-sepalwidth.png' alt='PetalLengthvsSepalWidth'>
</div> 
 
Finally, we see the measure of petal length to sepal width, we can observe similar trends, such as the generally wider sepal of the Setosa, and the longer petal of the Virginica.
Additionally, argument could be made for the existence of a weak correlation amongst the records of the Versicolor and Virginica flowers.


<h2>PART III: Summary</h2>
<div align='center'>
 <img src='https://github.com/ocoleman/pns-project2020/blob/master/plots/matrix.png' alt='Matrix'>
</div> 
 
 Trends that were observed amongst the histogram data were compounded by the results of the scatter plots. One such instance of this could be observed in the Iris’ sepal length, where significant overlap occurred alongside the existence of outliers among the Versicolors and Virginicas.
Conversely, initial indications implied the Setosas broad sepal would be one of the flowers key features, however further investigation showed this to be a less reliable metric for identifying the species. Despite this, the Iris Setosa time and again trended towards the left side of the axis. This leads me to conclude it is likely the smallest of the three flowers. The Virginica is probably the largest as was evident by its large features, such as possessing a longer and wider petal.
The Versicolor was found to be somewhere in the middle, although it often shared overlap with the Virginica, at times making it at times making the two indistinguishable (see Sepal Length). <b>Iris Setosa Statistics </b><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50.00000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.00000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.00600</td>
      <td>3.418000</td>
      <td>1.464000</td>
      <td>0.24400</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.35249</td>
      <td>0.381024</td>
      <td>0.173511</td>
      <td>0.10721</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.30000</td>
      <td>2.300000</td>
      <td>1.000000</td>
      <td>0.10000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.80000</td>
      <td>3.125000</td>
      <td>1.400000</td>
      <td>0.20000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.00000</td>
      <td>3.400000</td>
      <td>1.500000</td>
      <td>0.20000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.20000</td>
      <td>3.675000</td>
      <td>1.575000</td>
      <td>0.30000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.80000</td>
      <td>4.400000</td>
      <td>1.900000</td>
      <td>0.60000</td>
    </tr>
  </tbody>
</table><b>Iris Versicolor Statistics </b><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.936000</td>
      <td>2.770000</td>
      <td>4.260000</td>
      <td>1.326000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.516171</td>
      <td>0.313798</td>
      <td>0.469911</td>
      <td>0.197753</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.900000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.600000</td>
      <td>2.525000</td>
      <td>4.000000</td>
      <td>1.200000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.900000</td>
      <td>2.800000</td>
      <td>4.350000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.300000</td>
      <td>3.000000</td>
      <td>4.600000</td>
      <td>1.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.000000</td>
      <td>3.400000</td>
      <td>5.100000</td>
      <td>1.800000</td>
    </tr>
  </tbody>
</table><b>Iris Virginica Statistics </b><table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50.00000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.00000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.58800</td>
      <td>2.974000</td>
      <td>5.552000</td>
      <td>2.02600</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.63588</td>
      <td>0.322497</td>
      <td>0.551895</td>
      <td>0.27465</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.90000</td>
      <td>2.200000</td>
      <td>4.500000</td>
      <td>1.40000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>6.22500</td>
      <td>2.800000</td>
      <td>5.100000</td>
      <td>1.80000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.50000</td>
      <td>3.000000</td>
      <td>5.550000</td>
      <td>2.00000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.90000</td>
      <td>3.175000</td>
      <td>5.875000</td>
      <td>2.30000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.90000</td>
      <td>3.800000</td>
      <td>6.900000</td>
      <td>2.50000</td>
    </tr>
  </tbody>
</table>