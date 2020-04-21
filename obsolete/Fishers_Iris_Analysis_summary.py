
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os.path
iris_dataset = pd.read_csv("iris.csv")
iris_grps = iris_dataset.groupby("species")

def getiris(p1):
    iris = []
    iris = pd.read_csv(p1)
    return iris


def des():
    #iris = []
    #iris = pd.read_csv(p1)
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
#keep
#group by species
def descgrpsby():
    #iris_grps = iris_dataset.groupby("species")
    data = iris_grps.describe()
    return data.to_string()

def find_range(s):
    return s.max() - s.min()
#find the range
def comprange():
    data = iris_grps.aggregate(find_range)
    return data.to_string()



def std_dev(p1,p2):
    iris = []
    iris  = pd.read_csv(p1)
    return np.std(iris[p2])

def mean(p1,p2):
    iris = []
    iris  = pd.read_csv(p1)
    
    print(iris["setosa"])
    return np.mean(iris[p2])


    
    #return np.mean(iris[p2])

def median(p1,p2):
    iris = []
    iris = pd.read_csv(p1)
    return np.median(iris[p2])

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
        plt.savefig("summary_histogram_{}.png".format(var))
        print("Saved to file , summary_histogram_{}.png".format(var))
    except Exception as e:
        print("Histogram error " ,e)

def scatterplot(var,var1):
    try:
        iris = pd.read_csv("iris.csv")
        #iris.plot(kind = 'scatter', x=var, y=var1 )
        sns.set_style("whitegrid")
        sns.FacetGrid(iris,hue="species",height =8).map(plt.scatter,var,var1).add_legend()
        plt.legend()
        #plt.show()
        plt.savefig("summary_{}_{}_{}.png".format("Scatter_plot",var,var1))
        print("Saved to file , summary_{}_{}_{}.png".format("Scatter_plot",var,var1))
    except Exception as e:
        print("Scatterplot error",e)

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

#mean1("iris.csv")
#writeToAFile(descgrpsby("iris.csv"))
#des()
#grpsby("iris.csv")
writeToAFile("******************************** Summary ***********************************")
writeToAFile(descgrpsby())
writeToAFile("******************************** Range *************************************")
writeToAFile(comprange())
#writeToAFile("******************************* Mean ************************************** ")    
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
#writeToAFile("************************ Standard Deviation ****************************** ")
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
def medianVirginica():
    writeToAFile(formatoutput(mean("virginica_iris.csv","sepal_width"),"virginica","sepal_width","Mean"))
    writeToAFile(formatoutput(mean("virginica_iris.csv","sepal_length"),"virginica","sepal_length","Mean"))
    writeToAFile(formatoutput(mean("virginica_iris.csv","petal_length"),"virginica", "petal_lenght","Mean"))
    writeToAFile(formatoutput(mean("virginica_iris.csv","petal_width"),"virginica","petal_width","Mean"))


