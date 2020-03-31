#This is the b
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os.path
def displayDDmatrix():
    df = pd.read_csv('iris.csv')
    ax = plt.subplot()
    my_scatter_plot = ax.scatter(
        df["species"]
    )
    #dataset.head()
    #scatter_matrix(dataset)
    #plt.plot(dataset) 
    plt.show(my_scatter_plot)

def pairPlot():
    sns.set(style="whitegrid")
    iris = sns.load_dataset("iris")
    g = sns.pairplot(iris, hue="species",height=3)
    plt.show(g)
    
def pairPlot1():
    iris = pd.read_csv("iris.csv")
    g = sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, kind="kde", color="m")
    g.plot_joint(plt.scatter, c="w", s=40, linewidth=1, marker="+")
    g.ax_joint.collections[0].set_alpha(0)
    g.set_axis_labels("$SepalLength(Cm)$", "$SepalWidth(Cm)$") 
    plt.show()
def pairPlot2():
    iris = []
    iris = pd.read_csv("iris.csv")
    g = sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde", color="m")
    g.plot_joint(plt.scatter, c="w", s=40, linewidth=1, marker="+")
    g.ax_joint.collections[0].set_alpha(0)
    g.set_axis_labels("$SepalLength(Cm)$", "$SepalWidth(Cm)$") 
    plt.show()
def std_dev(p1,p2):
    iris = []
    iris  = pd.read_csv(p1)
    return np.std(iris[p2])
def mean(p1,p2):
    iris = []
    iris  = pd.read_csv(p1)
    return np.mean(iris[p2])


def formatoutput(p1,p2,p3,p4):
    #p1 is a number (mean)
    #p2 is a feild ie sepal width
    roundmean = round(p1,3)
    return "{} for species {} is {} {} ".format(p4,p2,p3,roundmean)


def writeToAFile(p1):
    if(os.path.isfile('summary.txt')):
        f = open("summary.txt","a")
        print("File exists",f)
        f.write("\n")#creates space between entries.
        f.write(p1)
        f.close()
    else:
        f = open("summary.txt","w")
        print("File not exits, has been create ",f)
        f.write(p1)
        f.close()
def meanVirginica():
    writeToAFile(formatoutput(mean("virginica_iris.csv","sepal_width"),"virginica","sepal_width","Mean"))
    writeToAFile(formatoutput(mean("virginica_iris.csv","sepal_length"),"virginica","sepal_length","Mean"))
    writeToAFile(formatoutput(mean("virginica_iris.csv","petal_length"),"virginica", "petal_lenght","Mean"))
    writeToAFile(formatoutput(mean("virginica_iris.csv","petal_width"),"virginica","petal_width","Mean"))
def meanVericolor():
    writeToAFile(formatoutput(mean("versicolor_iris.csv","sepal_width"),"versicolor","sepal_width","Mean"))
    writeToAFile(formatoutput(mean("versicolor_iris.csv","sepal_length"),"versicolor","sepal_length","Mean"))
    writeToAFile(formatoutput(mean("versicolor_iris.csv","petal_length"),"versicolor", "petal_lenght","Mean"))
    writeToAFile(formatoutput(mean("versicolor_iris.csv","petal_width"),"versicolor","petal_width","Mean"))
def meanSetosa():
    writeToAFile(formatoutput(mean("setosa_iris.csv","sepal_width"),"setosa","sepal_width","Mean"))
    writeToAFile(formatoutput(mean("setosa_iris.csv","sepal_length"),"setosa","sepal_length","Mean"))
    writeToAFile(formatoutput(mean("setosa_iris.csv","petal_length"),"setosa", "petal_lenght","Mean"))
    writeToAFile(formatoutput(mean("setosa_iris.csv","petal_width"),"setosa","petal_width","Mean"))

def stdDevVirginica():
    writeToAFile(formatoutput(std_dev("virginica_iris.csv","sepal_width"),"virginica","sepal_width","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("virginica_iris.csv","sepal_length"),"virginica","sepal_length","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("virginica_iris.csv","petal_length"),"virginica", "petal_lenght","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("virginica_iris.csv","petal_width"),"virginica","petal_width","Standard Deviation"))
def stdDevVericolor():
    writeToAFile(formatoutput(std_dev("versicolor_iris.csv","sepal_width"),"versicolor","sepal_width","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("versicolor_iris.csv","sepal_length"),"versicolor","sepal_length","Standard Deviation"))
    writeToAFile(formatoutput(mean("versicolor_iris.csv","petal_length"),"versicolor", "petal_lenght","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("versicolor_iris.csv","petal_width"),"versicolor","petal_width","Standard Deviation"))
def stdDevSetosa():
    writeToAFile(formatoutput(std_dev("setosa_iris.csv","sepal_width"),"setosa","sepal_width","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("setosa_iris.csv","sepal_length"),"setosa","sepal_length","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("setosa_iris.csv","petal_length"),"setosa", "petal_lenght","Standard Deviation"))
    writeToAFile(formatoutput(std_dev("setosa_iris.csv","petal_width"),"setosa","petal_width","Standard Deviation"))



#meanpl()
#meanpw()
#meansl()
#meansw()

