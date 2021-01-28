import pandas as pd
import plotly.express as px
import numpy as np
import csv
def getDataSource(data_path):
    Sleep=[]
    Coffee=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Sleep.append(float(row["Coffee in ml"]))
            Coffee.append(float(row["sleep in hours"]))
    return{"x":Coffee,"y":Sleep}
def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"]) 
    print("correlation=",correlation[0,1])
def plot():
    df= pd.read_csv("coffee.csv")
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()  
def setup():
    data_path="./coffee.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    
setup() 
plot()


















 