# -*- coding: utf-8 -*-
"""
Program to plot line graph,bar graph and box plot from the given dataset

"""
#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#Function to plot line graph
def lineGraph():
    plt.figure()
    plt.plot(df["Country Name"],df["1960"],label="1960")
    plt.plot(df["Country Name"],df["1980"],label="1980")
    plt.plot(df["Country Name"],df["2000"],label="2000")
    plt.plot(df["Country Name"],df["2020"],label="2020")
    #labelling x and y-axis
    plt.xlabel("Country")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.title("Life expectancy at birth")
    #saving the output graph in png format
    plt.savefig("line_graph.png")
    plt.show()
    
#Function to plot bar graph
def barGraph():
    plt.figure()
    plt.bar(df["Country Name"],df["1980"],label="1980",alpha=0.8,color="red")
    plt.bar(df["Country Name"],df["2000"],label="2000",alpha=0.4,color="blue")
    plt.bar(df["Country Name"],df["2020"],label="2020",alpha=0.4,color="green")
    plt.xlabel("Country")
    plt.ylabel("Life Expectancy")
    plt.legend()
    plt.title("Life expectancy at birth")
    plt.savefig("bar_graph.png")
    plt.show()
    
#Function to plot box plot
def boxPlot():
    plt.figure()
    dfs = pd.read_csv('life_expectancy_total.csv')
    #slicing the dataframe dfs
    data = dfs[30:40]
    print(data)
    plt.boxplot([data["1980"],data["2000"],data["2020"]],labels=["1960","2000","2020"]) 
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("Life expectancy at birth")
    plt.savefig("box_plot.png")
    plt.show()

#Read the csv file to the dataframe df and print it
df = pd.read_csv('life_expectancy.csv')
print(df)
#Calling different functions to plot data
lineGraph() 
barGraph()  
boxPlot()