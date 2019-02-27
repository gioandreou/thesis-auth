from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from pandas import ExcelWriter

def striplist(l):
    return([x.strip() for x in l])
    
def fetch_xlsx(dataframe):
    dataframe = dataframe.drop(['Date'], axis=1)
    headers=list(dataframe.columns.values)
    #print(headers)
    
    #item.replace(item, item.split(",")[1].strip())
    headers = [item.replace(item, item.split(",",1)[1]) for item in headers]
    headers = striplist(headers)
    #print(headers)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        dataframe.columns = headers
        dataframe = dataframe.groupby(dataframe.columns, axis=1).sum()
       
        #Mean values of regions
        dataframe_mean = dataframe.mean(axis=0 )
        dataframe_mean = dataframe_mean.nlargest(7)    
        
        '''
        #Latest values of regions
        dataframe_last = dataframe.drop(dataframe.index[:-1])
        dataframe_last = dataframe_last.transpose()
        column_name=list(dataframe_last.columns.values)
        dataframe_last = dataframe_last.nlargest(6,column_name[0])    
        '''
        writer = ExcelWriter('excels/lite/RegionDF.xlsx')
        dataframe_mean.to_excel(writer,'Sheet1')
        writer.save()        


def main():

    city_region = pd.read_excel('excels/lite/lite-City.xlsx')
    fetch_xlsx(city_region)

main()