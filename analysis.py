
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os.path
iris_dataset = pd.read_csv("iris.csv")
iris_grps = iris_dataset.groupby("species")

def des():
    data = iris_dataset.describe()
    print(data)
    return data.to_string()

#group by species
def grpsby(p1):
    iris = []
    iris = pd.read_csv(p1)
    iris_grps = iris.groupby("species")
    for name, data in iris_grps:
        print(name)
        print("----------------------------------------------------\n")
        print(data.iloc[:, 0:5])
        #print(data.iloc[0:4])
        print("\n")

#group by species
def descgrpsby():
    data = iris_grps.describe()
    return data.to_string()

#get the range
def find_range(s):
    return s.max() - s.min()

#find the range
def comprange():
    data = iris_grps.aggregate(find_range)
    return data.to_string()
#standard dev
def std_dev():
    data = iris_grps.std()
    return data.to_string()

#get the mean of each species
def iris_mean():
    data = iris_grps.mean()
    return data.to_string()

def iris_median():
    data = iris_grps.median()
    return data.to_string()
def quantile1():
    data = iris_grps.quantile(.25)
    return data.to_string()

def quantile3():
    data = iris_grps.quantile(.75)
    return data.to_string()
def quantile2():
    data = (iris_grps.quantile(.75) - iris_grps.quantile(.25))
    return data.to_string()

def formatoutput(p1,p2,p3,p4):
    #p1 is a number (mean)
    #p2 is a feild ie sepal width
    roundmean = round(p1,3)
    return "{} for species {} is {} {} ".format(p4,p2,p3,roundmean)

def historgram(var):
    try:
        data = pd.read_csv("iris.csv")
        iris = data[var]
        plt.hist(iris,bins=51,color = "green")
        plt.title("{} in cm".format(var)) 
        plt.xlabel("{}_cm".format(var)) 
        plt.ylabel("Count") 
        #plt.show()
        plt.savefig("histogram_{}.png".format(var))
        print("Saved to file ,histogram_{}.png".format(var))
    except Exception as e:
        print("Histogram error " ,e)

def scatterplot(var,var1):
    try:
        iris = pd.read_csv("iris.csv")
        #iris.plot(kind = 'scatter', x=var, y=var1 )
        sns.set_style("whitegrid")
        sns.FacetGrid(iris,hue="species",height =4).map(plt.scatter,var,var1).add_legend()
        plt.savefig("{}_{}_{}.png".format("Scatter_plot",var,var1))
        print("Saved to file ,{}_{}_{}.png".format("Scatter_plot",var,var1))
    except Exception as e:
        print("Scatterplot error",e)
def std_plot():
    sns.lmplot(x="sepal_length",y="sepal_width",hue="species",data=iris_dataset)
    #plt.show()
     #plt.savefig("summary_{}_{}_{}.png".format("Scatter_plot",var,var1))
       # print("Saved to file , summary_{}_{}_{}.png".format("Scatter_plot",var,var1)

def writeToAFile(p1):
    try:
        if(os.path.isfile('summary.txt')):
            f = open("summary.txt","a")
            f.write("\n")#creates space between entries.
            f.write(p1)
            f.close()
        else:
            f = open("summary.txt","w")
            f.write(p1)
            f.close()
    except IOError as err:
        print("File IO execption: " , err)

writeToAFile("******************************** Summary ***********************************")
writeToAFile(descgrpsby())
writeToAFile("******************************** Range *************************************")
writeToAFile(comprange())
writeToAFile("******************************** Mean ************************************** ")
writeToAFile(iris_mean())
writeToAFile("******************************** Median ************************************** ")
writeToAFile(iris_median())
writeToAFile("******************************** Standard Deviation ************************************** ")
writeToAFile(std_dev())
writeToAFile("******************************** First Quantile ************************************** ")
writeToAFile(quantile1())
writeToAFile("******************************** Thrid Quantile ************************************** ")
writeToAFile(quantile3())
writeToAFile("******************************** Inner Quantile range ************************************** ")
writeToAFile(quantile2())


