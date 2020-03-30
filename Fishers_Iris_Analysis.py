#This is the b
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
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
def mean():
    #unbeliveable this actually works. 
    print("Mean:")
    iris_setosa = []
    iris_setosa = pd.read_csv("setosa_iris.csv")
    print(np.mean(iris_setosa["petal_length"]))
#pairPlot()
mean()


