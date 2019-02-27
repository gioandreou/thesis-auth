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

def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)

def striplist(l):
    return([x.strip() for x in l])

def transpose(dataframe,condition): #FUNCTION THAT TRANSPOSES THE DATAFRMES CONDITION=1 (ONLY FOR TOP AGES DATAFRAME)
    if condition==1:
        dataframe = dataframe.iloc[:,1:].copy()
    else:
        dataframe = dataframe.iloc[:,:].copy()
    dataframe = dataframe.T
    return dataframe

def print_dataframes_education(regions,dataframe):
    border_msg('EDUCATIONAL STATS')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        regions_labels_list = list(regions.index) #LIST WITH THE REGIONS THAT EXIST IN FB PAGE
        
        region_df = pd.DataFrame() #NEW DF TO STORE THE FORMATED DATA
        region_df['Total']=dataframe['Total']
        
        #HIGHER EDUCATION = SUM OF PEOPLE THAT ARE IN PHD+MASTERS+BACHERLOR+ATEI LEVEL
        #MIDDLE EDUCATION = SUM OF PEOPLE THAT ARE IN UPRS+IEK+HIGH SCHOOL+ VUPS+VPS LEVEL
        #LOWER EDUCATION = SUM OF PEOPLE THAT ARE IN MIDDLE SCHOOL + ELEMENTARY SCHOOL + ABANDONED +ILITERATE LEVEL
        higher_edu = (dataframe['PhD']+dataframe['Masters']+dataframe['Bachelor']+dataframe['Technological Educational Institute'])
        middle_edu = (dataframe['Upper Vocational Private Schools']+dataframe['Institute Vocational Training - IEK']+dataframe['High School']+dataframe['Vocational upper secondary schools']+dataframe['Vocational Private Schools'])
        lower_edu = (dataframe['Middle School\n']+dataframe['Elementary School']+dataframe['Abandoned Elementary - Can Read Write']+dataframe['Illeterate'])
        
        #CALCULATE THE PERCENTS OF EACH CATEGORY
        percen_higher = ((higher_edu/dataframe['Total'])*100).round(2)
        percen_middle = ((middle_edu/dataframe['Total'])*100).round(2)
        percen_lower = ((lower_edu/dataframe['Total'])*100).round(2)

        #FORMATION IN DF : VALUE--[PERCENT OF VALUE%]
        region_df['Higher Education']= (higher_edu.map(str)+"--["+percen_higher.map(str)+ "%]")
        region_df['Middle Education']= (middle_edu.map(str)+"--["+percen_middle.map(str)+ "%]")
        region_df['Lower Education']= (lower_edu.map(str)+"--["+percen_lower.map(str)+ "%]")
        
        #PERCENTAGES WILL BE USED IN FANS PERCENTAGE CORELLATION 
        region_df['Higher Education Percentage[%]']= percen_higher
        region_df['Middle Education Percentage[%]']= percen_middle
        region_df['Lower Education Percentage[%]']= percen_lower
        
        #ALL THE REGIONS IN GREECE THAT FB CAN USE. UNUSED 
        #print(regions_labels_list)
        #print(region_df)
        
        
        for item in regions_labels_list:
            print("\n\n")
            print(50*"--")
            #PRINT REGION 
            print(item) 
            #PRINT THE STATS OF ELSTAT FOR THIS REGION
            print(region_df.loc[(item),['Total','Higher Education','Middle Education','Lower Education']])
            print("\nFacebook Page Correlation:\n")
            
            #ADD A LEADING WHITESPACE TO THE NAME INORDER TO BE MATCHED WITH THE INDEXES OF THE REGIONS DF
            #region = " "+item 
            value = regions.loc[(item),:].item()

            #PASS THE VALUES OF MALES AND FEMALES FOR HIGHER, MID, LOWER EDUCATION 
            higher_percent_male = region_df.loc[(item),['Higher Education Percentage[%]']].values[0]
            higher_percent_female = region_df.loc[(item),['Higher Education Percentage[%]']].values[1]

            middle_percent_male = region_df.loc[(item),['Middle Education Percentage[%]']].values[0]
            middle_percent_female = region_df.loc[(item),['Middle Education Percentage[%]']].values[1]

            lower_percent_male = region_df.loc[(item),['Lower Education Percentage[%]']].values[0]
            lower_percent_female = region_df.loc[(item),['Lower Education Percentage[%]']].values[1]
            
            #PRETTY PRINTING
            print("Higher Edu: Male={a}\t Female={b}\t".format(
                a=(value*higher_percent_male/100).round(2), 
                b=(value*higher_percent_female/100).round(2), 
                ))
            print("Middle Edu: Male={a}\t Female={b}\t".format(
                a=(value*middle_percent_male/100).round(2), 
                b=(value*middle_percent_female/100).round(2), 
                ))
            print("Lower Edu: Male={a}\t Female={b}\t".format(
                a=(value*lower_percent_male/100).round(2), 
                b=(value*lower_percent_female/100).round(2), 
                ))
        border_msg('END OF EDUCATIONAL STATS')

def print_dataframe_age_occupation(regions,dataframe):
    border_msg('AGE AND OCCUPATIONAL STATS')
    #LOAD AGE DATAFRAME 
    age_dataframe = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')
    transp_age_df = transpose(age_dataframe,1)
    
    #GET THE TOTAL SUM OF ROWS
    total = np.sum(transp_age_df.iloc[:,:].values)
    transp_age_df['percent'] = transp_age_df.iloc[:,:].sum(axis=1)/total * 100
    
    #FIND AND KEEP THE N LARGEST AGE-GROUPS BY 'PERCENT'
    df_ages_top = transp_age_df.nlargest(4, 'percent')
    #DROP THE REST COLUMNS
    df_ages_final = df_ages_top.drop(df_ages_top.columns[0:-1], axis=1)
    ages_list = list(df_ages_final.index)
   
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        
        #INITIALISE NEW DF
        ages_df = pd.DataFrame()
        
        #APPEND-JOIN ALL AGES IN TO A SINGLE ONE DF
        for item in ages_list:
            temp = dataframe.loc[(item),:]
            ages_df = ages_df.join(temp, how='outer')    
        
        #TRANSPOSE TO CHANGE COL<->ROW
        ages_trans_df = transpose(ages_df,2)

        #INITIALISE NEW DF
        percentages_ages_df = pd.DataFrame()
        #ADD TO THE DF THE FOLLOWING COLUMNS (VALUE/TOTAL %)
        percentages_ages_df['Total Active %']= ((ages_trans_df['Total Active']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Employed\n %']= ((ages_trans_df['Employed\n']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Unemployed Total %']= ((ages_trans_df['Unemployed Total']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Unemployed Former Employed %']= ((ages_trans_df['Unemployed Former Employed']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Non Active Total %']= ((ages_trans_df['Non Active Total']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Non Active Students %']= ((ages_trans_df['Non Active Students']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Non Active Retired\n %']= ((ages_trans_df['Non Active Retired\n']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Non Active Rentier\n %']= ((ages_trans_df['Non Active Rentier\n']/ages_trans_df['Total'])*100).round(2)
        percentages_ages_df['Non Active Housekeeping %']= ((ages_trans_df['Non Active Housekeeping']/ages_trans_df['Total'])*100).round(2)
        
        print(percentages_ages_df)

        #print(dataframe.loc[('Female', 'F.13-17'),:])
    border_msg('END OF AGE AND OCCUPATIONAL STATS')

def print_dataframe_family(regions,dataframe):
    border_msg('FAMILY STATUS STATS')
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        intial_region_list = list(regions.index) #LIST WITH THE REGIONS THAT EXIST IN FB PAGE
        regions_labels_list=striplist(intial_region_list) #LIST ITEMS WITHOUT LEADING SPACE E.X." NAME"

        regions_family_df = pd.DataFrame() #NEW DF TO STORE THE FORMATED DATA
        #ADD COLUMNS TO THE DF WITH THE STATS FROM ELSTAT
        regions_family_df['Both Genders Non Married %']=((dataframe['Both Genders Non Married']/dataframe['Total'])*100).round(2)
        regions_family_df['Both Genders Married %']=((dataframe['Both Genders Married']/dataframe['Total'])*100).round(2)
        regions_family_df['Both Genders Widower %']=((dataframe['Both Genders Widower\n']/dataframe['Total'])*100).round(2)
        regions_family_df['Both Genders Divorced %']=((dataframe['Both Genders Divorced']/dataframe['Total'])*100).round(2)
        regions_family_df['Both Genders Civil Partnership %']=((dataframe['Both Genders Civil Partnership\n']/dataframe['Total'])*100).round(2)
        regions_family_df['Both Genders Separated %']=((dataframe['Both Genders Separated']/dataframe['Total'])*100).round(2)
        regions_family_df['Both Genders Widower From Civil Partnership %']=((dataframe['Both Genders Widower From Civil Partnership']/dataframe['Total'])*100).round(2)
        regions_family_df['Both Genders Separated From Civil Partnership %']=((dataframe['Both Genders Separated From Civil Partnership']/dataframe['Total'])*100).round(2)

        #ITERATE THROUGH EVERY REGION IN THE LIST
        for item in regions_labels_list:
            print("\n\n")
            print(50*"--")
            #PRINT REGION 
            print(item) 
            #PRINT THE STATS OF ELSTAT FOR THIS REGION
            print(regions_family_df.loc[(item),:])#PRINT THE DF WITH THE STATS OF ELSTAT
            print("\nFacebook Page Correlation:\n")
            #VALUE = NUMBER OF FANS OF EACH REGION
            value = regions.loc[(item),:].item()
            #PRINTING THE STATS OF THE FB PAGE (NUMBER OF FANS * PERCENTAGE OF ELSTAT)
            print("Fans of Both Genders Non Married in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Non Married %']].values[0]/100).round(0)))
            print("Fans of Both Genders Married in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Married %']].values[0]/100).round(0)))
            print("Fans of Both Genders Widower in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Widower %']].values[0]/100).round(0)))
            print("Fans of Both Genders Divorced in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Divorced %']].values[0]/100).round(0)))
            print("Fans of Both Genders Civil Partnership in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Civil Partnership %']].values[0]/100).round(0)))
            print("Fans of Both Genders Separated in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Separated %']].values[0]/100).round(0)))
            print("Fans of Both Genders Widower From Civil Partnership in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Widower From Civil Partnership %']].values[0]/100).round(0)))
            print("Fans of Both Genders Separated From Civil Partnership in FB Page :\t{a}".format(a=(value*regions_family_df.loc[(item),['Both Genders Separated From Civil Partnership %']].values[0]/100).round(0)))
            



        #print(dataframe)
        #print(regions)

    border_msg('END OF FAMILY STATUS STATS')
def main():

    regions = pd.read_excel('excels/lite/RegionDF.xlsx')
    
    education = pd.read_excel('excels/elstat/formated epipedo ekpaideusis.xlsx')
    print_dataframes_education(regions,education)
    
    occupation = pd.read_excel('excels/elstat/formated katastasi asxolias greece.xlsx')
    print_dataframe_age_occupation(regions,occupation)
    
    family = pd.read_excel('excels/elstat/formated oikogeneiaki katastasi.xlsx')
    print_dataframe_family(regions,family)
    


main()