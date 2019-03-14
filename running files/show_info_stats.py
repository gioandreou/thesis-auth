from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as dates
from os import listdir
from os.path import isfile, join


def transpose(dataframe):
    dataframe = dataframe.iloc[:,1:].copy()
    dataframe = dataframe.T
    return dataframe

def get_excel_to_panda(path_excel):

    dataframe = pd.read_excel(path_excel)
    return dataframe

def dataframe_ages(age_dataframe):

    new_df = transpose(age_dataframe)

    total = np.sum(new_df.iloc[:,:].values)
    new_df['percent'] = new_df.iloc[:,:].sum(axis=1)/total * 100
    
    #indexNamesArr = new_df.index.values
    #listOfRowIndexLabels = list(indexNamesArr)

    df_ages_top = new_df.nlargest(4, 'percent')
    df_ages_final = df_ages_top.drop(df_ages_top.columns[0:-1], axis=1)
    print_ages_df(df_ages_final)

def print_ages_df(dataframe):
    count_row = dataframe.shape[0] 
    print("\n\nThese are the top {num} Ages stats of the page\n\n".format(num=count_row))
    print(dataframe)
    print(50*"--")

def print_page_post(dataframe,start,end):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print("\n\nThese are the Page-Post stats of the page from start-date: {start}  to end-date: {end} \n\n".format(start=start,end=end))
        print(dataframe)
        print(50*"--")

def print_page_info(dataframe,start,end):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print("\n\nThese are the info Page stats of the page from start-date: {start}  to end-date: {end} \n\n".format(start=start,end=end))
        print(dataframe)
        print(50*"--")

def dataframe_page_info(dataframe):
    
    new_df = transpose(dataframe)
    list_df_labels = list(new_df.T)
    #print(list_df_labels)

    col_lenght= len(new_df.columns)
    start = str(dataframe['Date'].iloc[0])
    end = str(dataframe['Date'].iloc[-1])

    new_df['start']=new_df.iloc[:,0]
    new_df['end']=new_df.iloc[:,col_lenght-1]
    new_df['mean']=new_df.mean(axis=1)
    new_df['growth in %']= ((new_df['end']-new_df['start'])/new_df['start'])*100
    
    new_df['Largest Value']=dataframe.max(axis=0)
    
    largest_value_list = []
    for label in list_df_labels:
        largest_value_list.append(dataframe['Date'][dataframe[label].idxmax()])
    new_df['Largest Value at']=largest_value_list
    new_df = new_df.drop(new_df.columns[0:-6], axis=1)
    return(new_df,start,end)

def dataframe_post_info(dataframe):
    post_dataframe = dataframe[['Message','Date']].copy()
    
    percen_paid = ((dataframe['Impressions Paid']/dataframe['Impressions'])*100).round(2)
    percen_org = ((dataframe['Impressions Organic']/dataframe['Impressions'])*100).round(2)
    percen_vir = ((dataframe['Impressions Viral']/dataframe['Impressions'])*100).round(2)
    percen_paid_fan = ((dataframe['Impressions Fans Paid']/dataframe['Impressions Fans'])*100).round(2)

    df_to_pass_imp=(
        dataframe['Impressions'].map(str)+"--("+ dataframe['Impressions Paid'].map(str)+ ")["+
        percen_paid.map(str)+ "%]--(" +dataframe['Impressions Organic'].map(str)+ ")[" +
        percen_org.map(str)+ "%]--(" +dataframe['Impressions Viral'].map(str)+")[" +
        percen_vir.map(str)+ "%]"
    )
    post_dataframe['Impressions(Paid)[%](Organic)[%](Viral)[%]']=df_to_pass_imp
    
    df_to_pass_imp_fan=(
        dataframe['Impressions Fans'].map(str)+"--("+dataframe['Impressions Fans Paid'].map(str)+ ")["+
        percen_paid_fan.map(str)+ "%]"
    )
    post_dataframe['Impressions Fans (Paid)[%]']=df_to_pass_imp_fan
    post_dataframe['Reactions']=dataframe['Total Reactions']
    post_dataframe['Enganged Users']=dataframe['Enganged Users']

    print_post_info (post_dataframe)

def print_post_info(dataframe):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print("\n\nThese are the Post stats of the page  \n\n")
        print(dataframe)
        print(50*"--")

def dataframe_city_country(dataframe,typedf):
        start = str(dataframe['Date'].iloc[0])
        end = str(dataframe['Date'].iloc[-1])

        #dataframe.encode('ascii', 'ignore')
        #print(start)

        last_date_top = transpose(dataframe)
        last_date_top = last_date_top.nlargest(5,0)
        first_values= last_date_top.iloc[:,0]
        last_values = last_date_top.iloc[:,-1]

        new_df = pd.DataFrame()
        new_df['First Count'] = first_values
        new_df['Last Count'] = last_values
        new_df['Growth %'] = (((last_values-first_values)/last_values)*100).round(2)
        #print(new_df)
        #last_date_top = end


        print_locale_city_country(new_df,typedf)

def print_locale_city_country(dataframe,typedf):
        with pd.option_context('display.encoding', 'UTF-8', 'display.max_rows', 100, 'display.max_columns', None):
                print("\n\nThese are the {a} stats of the page  \n\n".format(a=typedf))
                print(dataframe)
                print(50*"--")

def main():
    
        mypath="excels/lite/"
        list_of_excel_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(list_of_excel_files)

        df_dict={}

        for item in list_of_excel_files:
                path=mypath+item

                temp_dict = {item : get_excel_to_panda(path)}
                df_dict.update(temp_dict)


        df_country=df_dict['lite-Country.xlsx']
        df_city=df_dict['lite-City.xlsx']
        df_locale = df_dict['lite-Locale.xlsx']        
        df_page_info=df_dict['lite-Page-Info.xlsx']
        df_post=df_dict['lite-Post-Info.xlsx']
        df_ages=df_dict['lite-Ages-Gender.xlsx']
        df_page_post_info= df_dict['lite-Page-Post.xlsx']
        
        df_info,start_info,end_info =  dataframe_page_info(df_page_info)
        print_page_info(df_info,start_info,end_info)

        df_info,start_info,end_info =  dataframe_page_info(df_page_post_info)
        print_page_post(df_info,start_info,end_info)

        dataframe_post_info(df_post)
        dataframe_ages(df_ages)
        
        dataframe_city_country(df_country,"Country")
        '''
        #ascii problem
        dataframe_city_country(df_city,"City")
        '''
        dataframe_city_country(df_locale,"Locale")
    
main()