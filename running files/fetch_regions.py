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
    #DROP THE DATE COLUMN TO KEEP ONLY THE CITY-REGION VALUES
    dataframe = dataframe.drop(['Date'], axis=1)
    headers=list(dataframe.columns.values)
    
    #KEEP THE SECOND PART OF THE STRING e.g. "Thessaloniki, Central Macedonia, Greece" -> " Central Macedonia, Greece"
    headers = [item.replace(item, item.split(",",1)[1]) for item in headers]
    
    #DELETE THE LEADING WHITESPACE FROM THE STRING e.g. " Central Macedonia, Greece"-> "Central Macedonia, Greece"
    headers = striplist(headers)
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        dataframe.columns = headers
        #GROUP DATA BY THEIR COLUMNS(REGIONS) AND SUM TOGETHER THE COLUMNS(REGIONS) WITH THE SAME NAME .
        dataframe = dataframe.groupby(dataframe.columns, axis=1).sum()
       
        #CALCULATE THE MEAN VALUE FOR EVERY REGION
        dataframe_mean = dataframe.mean(axis=0 )
        #KEEP THE N LARGEST REGIONS 
        dataframe_mean = dataframe_mean.nlargest(7)    
        
        #COMMENTED OUT OPTION, TO KEEP THE LATEST VALUES OF THE DATAFRAME
        '''
        #Latest values of regions
        dataframe_last = dataframe.drop(dataframe.index[:-1])
        dataframe_last = dataframe_last.transpose()
        column_name=list(dataframe_last.columns.values)
        dataframe_last = dataframe_last.nlargest(6,column_name[0])    
        '''
        #WRITE THE DF TO XLSX IN ORDER TO BE PARSED BY OTHER FILES 
        writer = ExcelWriter('excels/lite/RegionDF.xlsx')
        dataframe_mean.to_excel(writer,'Sheet1')
        writer.save()        


def main():

        #PARSE THE XLSX TO DATAFRAME
    city_region = pd.read_excel('excels/lite/lite-City.xlsx')
    fetch_xlsx(city_region)

main()