from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import plotly.graph_objs as go
import plotly.io as pio
from tabulate import tabulate

def striplist(l):
    return([x.strip() for x in l])


def print_dataframes_education(regions,dataframe):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        intial_region_list = list(regions.index)
        regions_labels_list=striplist(intial_region_list)
        
        region_df = pd.DataFrame()
        region_df['Total']=dataframe['Total']
        
        higher_edu = (dataframe['PhD']+dataframe['Masters']+dataframe['Bachelor']+dataframe['Technological Educational Institute'])
        middle_edu = (dataframe['Upper Vocational Private Schools']+dataframe['Institute Vocational Training - IEK']+dataframe['High School']+dataframe['Vocational upper secondary schools']+dataframe['Vocational Private Schools'])
        lower_edu = (dataframe['Middle School\n']+dataframe['Elementary School']+dataframe['Abandoned Elementary - Can Read Write']+dataframe['Illeterate'])

        percen_higher = ((higher_edu/dataframe['Total'])*100).round(2)
        percen_middle = ((middle_edu/dataframe['Total'])*100).round(2)
        percen_lower = ((lower_edu/dataframe['Total'])*100).round(2)


        region_df['Higher Education']= (higher_edu.map(str)+"--["+percen_higher.map(str)+ "%]")
        region_df['Middle Education']= (middle_edu.map(str)+"--["+percen_middle.map(str)+ "%]")
        region_df['Lower Education']= (lower_edu.map(str)+"--["+percen_lower.map(str)+ "%]")
        region_df['Higher Education Percentage[%]']= percen_higher
        region_df['Middle Education Percentage[%]']= percen_middle
        region_df['Lower Education Percentage[%]']= percen_lower
        
        all_regions_label_list = ['Greece','Eastern Macedonia and Thrace, Greece','Central Macedonia, Greece','Western Macedonia, Greece','Epirus (region), Greece','Thessaly, Greece','Central Greece (region), Greece',
                                'Ionian Islands (region), Greece','Western Greece, Greece','Peloponnese (region), Greece','Attica (region), Greece','Northern Aegean, Greece','Southern Aegean, Greece','Crete, Greece']
        '''
        print(intial_region_list)
        print(regions.loc[(intial_region_list[0]),:]) ##sos thelei keno prin to label
        '''
        for item in regions_labels_list:
            print("\n\n")
            print(50*"--")
            print(item)
            print(region_df.loc[(item),['Total','Higher Education','Middle Education','Lower Education']])
            print("\nFacebook Page Correlation:\n")
            region = " "+item 
            value = regions.loc[(region),:].item()

            #print("Fans: {a}".format(a=value))
            higher_percent_male = region_df.loc[(item),['Higher Education Percentage[%]']].values[0]
            higher_percent_female = region_df.loc[(item),['Higher Education Percentage[%]']].values[1]

            middle_percent_male = region_df.loc[(item),['Middle Education Percentage[%]']].values[0]
            middle_percent_female = region_df.loc[(item),['Middle Education Percentage[%]']].values[1]

            lower_percent_male = region_df.loc[(item),['Lower Education Percentage[%]']].values[0]
            lower_percent_female = region_df.loc[(item),['Lower Education Percentage[%]']].values[1]
            
            print("Higher Edu: Male={a}\t Female={b}\t".format(
                a=value*higher_percent_male/100, 
                b=value*higher_percent_female/100, 
                ))
            print("Middle Edu: Male={a}\t Female={b}\t".format(
                a=value*middle_percent_male/100, 
                b=value*middle_percent_female/100, 
                ))
            print("Lower Edu: Male={a}\t Female={b}\t".format(
                a=value*lower_percent_male/100, 
                b=value*lower_percent_female/100, 
                ))
            
        

def main():

    regions = pd.read_excel('excels/lite/RegionDF.xlsx')
    

    education = pd.read_excel('excels/elstat/formated epipedo ekpaideusis.xlsx')
    print_dataframes_education(regions,education)






main()