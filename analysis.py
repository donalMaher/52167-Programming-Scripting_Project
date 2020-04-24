
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os.path
iris_dataset = pd.read_csv("iris.csv")
iris_grps = iris_dataset.groupby("species")

#the pair plot
def pair_plot():
    sns.set_style("whitegrid")
    sns.pairplot(iris_dataset,hue="species" ,height=3,diag_kind="hist")
    plt.savefig("pairPlot.png")



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

#get the median of each species
def iris_median():
    data = iris_grps.median()
    return data.to_string()

#get the 1st quantile 
def quantile1():
    data = iris_grps.quantile(.25)
    return data.to_string()
#get the 3rd quantile
def quantile3():
    data = iris_grps.quantile(.75)
    return data.to_string()
# inner quantile range
def quantile2():
    data = (iris_grps.quantile(.75) - iris_grps.quantile(.25))
    return data.to_string()

def formatoutput(p1,p2,p3,p4):
    #p1 is a number (mean)
    #p2 is a feild ie sepal width
    roundmean = round(p1,3)
    return "{} for species {} is {} {} ".format(p4,p2,p3,roundmean)

def historgram1():
    try:
        counter = 0
        while counter != 4:
            variables = ["sepal_length","sepal_width","petal_length","petal_width"]
            #color = ["green","orange", "red","black",]
            data = pd.read_csv("iris.csv")
            iris = data[variables[counter]]
            plt.hist(iris,bins=10,color="orange")
            plt.title("{} in cm".format(variables[counter])) 
            plt.xlabel("{}_cm".format(variables[counter])) 
            plt.ylabel("Count")
            #plt.legend(var) 
            #plt.show()
            plt.savefig("histogram_{}.png".format(variables[counter]))
            print("Saved to file ,histogram_{}.png".format(variables[counter]))
            counter += 1
    except Exception as e:
        print("Histogram error " ,e)
#This function will create four histograms. 
def histogram():
    #Try this code and catch any exections
    try:
        #Create a array of column names so the caller will not have to pass them in 
        var = ["petal_length","petal_width","sepal_length","sepal_width"]
        x = len(var)
        i=0
        # dataset already imported
        iris = iris_dataset
        #create an seaborn facegrid on each species
        g=sns.FacetGrid(iris,col="species")
        # loop to create the histograms and save to a file.
        while i != x:
            g.map(plt.hist,var[i],bins=5,color="green")
            g.set(ylabel="Count")
            plt.savefig("{}_{}.png".format("histogram",var[i]))
            i+=1
    except Exception as e:
        print("Histogram error " ,e)
  
#Scatter plot
#uses Seaborn FacetGrid class. This useful when you want to visualize the 
# distribution of a variable or the relationship 
# between multiple variables separately within subsets of your dataset. 
# A FacetGrid can be drawn with up to three dimensions: row, col, and hue. 
# The first two have obvious correspondence with the resulting array of axes; 
# think of the hue variable as a third dimension along a depth axis, 
# where different levels are plotted with different colors.
def scatterplot(var,var1):
    #try and catch execptions
    try:
        iris = iris_dataset
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


