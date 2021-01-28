import pandas as pd
import plotly.express as px
import numpy as np
import csv
def getDataSource(data_path):
    Days=[]
    Marks=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Days.append(float(row["Marks In Percentage"]))
            Marks.append(float(row["Days Present"]))
    return{"x":Marks,"y":Days}
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"]) 
    print("correlation=",correlation[0,1])
def plot():
    df= pd.read_csv("students.csv")
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()  
def setup():
    data_path="./students.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    
setup() 
plot()


















 