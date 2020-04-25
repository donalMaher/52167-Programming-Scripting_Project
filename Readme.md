# Programming and Scripting 2020 Project

## Abstract

Using Python libraries imported into a python script to create a summary of each variable that included the Range, Mean, Median, Standard Deviation and the Quartiles. Each species variables displayed with Histograms, Scatterplots and Pair Plot.

The results of this investigation will show how using python to examine the Fishers Dataset can lead to a better and faster analysis.

## Introduction

This project is an investigation into the Fishers Iris Dataset. While this dataset is a corner stone in the data analysis this project will use it to present the usefulness of python in data analysis. This dataset is widely used to teach students techniques in statistics. The dataset is of good quality and without missing fields.

Objectives of this project will be to:

- Explain the benefits of using Python in the analysis of datasets.
- Present the results of data analysis using the Fishers dataset
- Research Fishers Linear Discriminant Analysis(LDA)
- To present the code that will show to the user the benefits of ease of use of python in data analysis.
- And to expand knowledge of data analysis and python.

This was accomplished by import various libraries into python using the Visual studio IDE, the project will be version controlled with Git hub. This project will be presented in such a way as to allow a person or group that are not familiar with python to grasp the ease of python when analysing data.

## Materials and Methods

1. Python:
  1. Pandas: this fast, powerful and flexible open source software used for data analysis and manipulation tool. [pandas](https://pandas.pydata.org/)
  2. Matplotlib: Is a library for creating static, animated and interactive visualization in Python. [matplotlib](https://matplotlib.org/)
  3. Numpy: This library is a fundamental package for scientific computing. [numpy](https://numpy.org/)
  4. Seaborn: Used in Python for data statistical data visualization library based on matplotlib. [seaborn](https://seaborn.pydata.org/)
2. Fishers Iris Dataset:
3. GitHub: [GitHub](https://github.com/donalMaher/52167-Programming-Scripting\_Project)
4. Running the code: Navigate to where you have download the python script via your command prompt run the command "python analysis_test.py" prerequisite, must have python installed on your computer.

![Figure1](Running the code.png)

## Results

The results of call the python script are shown here:


Histogram: petal length 
![Figure 2 Histogram petal length](histogram_petal_length.png)
![Figure 3 Histogram petal width](histogram_petal_width.png)
![Figure 4 Histogram Sepal Length ](histogram_sepal_length.png)
![Figure 5 Histogram Sepal width](histogram_sepal_width.png) 
![Figure 6 Petal length vs Petal width ](Scatter_plot_petal_length_petal_width.png)
![Figure 7 sepal length vs sepal width](Scatter_plot_sepal_length_sepal_width.png)
 
Pair Plot
 ![](pairPlot.png)
Figure 8 Pair plot
Code ![](RackMultipart20200424-4-tjis8w_html_c6762d5066ee19bc.gif)

## Discussion

### Investigation:

The analysis of the dataset will be a compressive summary of the data contained with.

The summary statistics:

There are four key areas is a summary

1. Centrality: the middle value or average
2. Dispersion: how the spread out the values are from the average
3. Replication: how many values there are in the sample
4. Shape: The data distribution.

#### Centrality:

The Average is an important measure is statically analysis. It gives an idea about where the data seems to be clustered around. In this summary the mean and the median was calculated.

1. Mean:
![](images/Mean.PNG)

It can be seen that with two lines of code the mean of the species variable can be displayed.

1. Median:

The mean is average of the values. The median is the measure of central tendency number in a sorted list. The advantage of the median over the mean the median is not skewed so much by extremely large or small values.

![Median](images/Median.PNG)


#### Dispersion:

How spread out the values are around the average. If the values are close that to the average, and then the iris dataset grouped by species has low dispersion and the opposite for high.

There are several choices to get the dispersion. This summary has the following:

1. Standard Deviation :

This is used when the data is normally distributed. An, average deviation from the mean.

In python its not difficult to calculate this.

Standard Deviation:

This means that the standard deviation is less that 1 standard deviation from the mean.

Code:
![](images/standard.PNG)

1. Inter-Quartile range (IQR)

Used when the data that is not normally distributed

1. Inter- Quartile range:

![](images/InnerQRange.PNG)
1. Range

The range is the difference between the max and the min values

![](images/Range.PNG)

#### Replication:

The simples form of summary statistics but its important. Its simply the number of observations.

#### Shape

The shape of the data affects the type of summary statistics that best summarize them. The &quot;shape&quot; refers to how the data values are distributed across the range of values in the sample. Generally you expect there to be a &quot;cluster&quot; of values around the average. It is important to know if the values are more or less symmetrically arranged around the average, or if there are more values to one side than the other.

##### Histogram:

The histogram: represents the frequency distribution of data point. Frequency distribution is useful for showing the occurrence of a variable.

In figure 1, the axis y is count and x axis is. In the figures show length and width show no Determining of the species. Even if the data was cluster in the species

Code:

![](images/Range.PNG)

Figure 9 Histogram code

_ **The scatter plot** _:

This 2 dimensional plot shows the sepal length and sepal width it&#39;s clear that the blue points are easily determining one of the species, but the other 2 cannot be identified as individual species as they cannot be separated from each other

Linear discriminant analysis:
