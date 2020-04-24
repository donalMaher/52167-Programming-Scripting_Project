import analysis
#Create historgram
analysis.histogram()
#Create scatterplot
analysis.scatterplot("sepal_length","sepal_width")
analysis.scatterplot("petal_length","petal_width")
analysis.pair_plot()
#Create summary.txt
analysis.writeToAFile



