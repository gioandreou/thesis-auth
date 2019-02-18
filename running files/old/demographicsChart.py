from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d} )".format(pct, absolute)
labels_Ages=['13-17','18-24','25-34','35-44','45-54','55-64','65+']

def plot_ages_content(dataframe):
    #print(dataframe)
    #                       iloc[rows,cols]     
    date_content=dataframe.iloc[:,0:1]
    women_age =  dataframe.iloc[:,1:8].mean()
    men_age=dataframe.iloc[:,8:15].mean()

    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
    women_age.plot.pie(labels=['F.13-17','F.18-24','F.25-34','F.35-44','F.45-54','F.55-64','F.65+'],
    fontsize=8,subplots=True, autopct=lambda pct:func(pct,women_age.values),
    textprops=dict(color="w"))
    ax.set_title("Average Women Age Chart for Content Activity"+date_content.iat[0,0].split("T",1)[0]+" until "+date_content.iat[-1,0].split("T",1)[0],fontsize=15)
    ax.set_ylabel('Chart')
    ax.set_xlabel('Average Percentage and (number of people)')
    ax.legend(labels=labels_Ages,
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    plt.savefig("charts/Women-Age-Content"+".png",dpi=300)
    print("Women : Age-Content chart was created!")
    
    plt.clf()
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
    
    men_age.plot.pie(labels=['M.13-17','M.18-24','M.25-34','M.35-44','M.45-54','M.55-64','M.65+'],
    fontsize=8,subplots=True, autopct=lambda pct:func(pct,men_age.values),
    textprops=dict(color="w"),pctdistance=0.7)
    ax.set_title("Average Men Age Chart for Content Activity"+date_content.iat[0,0].split("T",1)[0]+" until "+date_content.iat[-1,0].split("T",1)[0],fontsize=15)
    ax.set_ylabel('Chart')
    ax.set_xlabel('Average Percentage and (number of people)')
    ax.legend(labels=labels_Ages,
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    plt.savefig("charts/Men-Age-Content"+".png",dpi=300)
    print("Men : Age-Content chart was created!")
    plt.clf()
    
 
def plot_ages_impressions(dataframe):
    women_age =  dataframe.iloc[:,1:8].mean()
    men_age=dataframe.iloc[:,8:15].mean()
    date_impression = dataframe.iloc[:,0:1]

    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
    women_age.plot.pie(labels=['F.13-17','F.18-24','F.25-34','F.35-44','F.45-54','F.55-64','F.65+'],
    fontsize=8,subplots=True, autopct=lambda pct:func(pct,women_age.values),
    textprops=dict(color="w"),pctdistance=0.7)
    ax.set_title("Average Women Age Chart for Impression"+date_impression.iat[0,0].split("T",1)[0]+" until "+date_impression.iat[-1,0].split("T",1)[0],fontsize=15)
    ax.set_ylabel('Chart')
    ax.set_xlabel('Average Percentage and (number of people)')
    ax.legend(labels=labels_Ages,
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    plt.savefig("charts/Women-Age-Impression"+".png",dpi=300)
    print("Women : Age-Impression chart was created!")

    plt.clf()
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
    
    men_age.plot.pie(labels=['M.13-17','M.18-24','M.25-34','M.35-44','M.45-54','M.55-64','M.65+'],
    fontsize=8,subplots=True, autopct=lambda pct:func(pct,men_age.values),
    textprops=dict(color="w"),pctdistance=0.7)
    ax.set_title("Average Men Age Chart for Impressions"+date_impression.iat[0,0].split("T",1)[0]+" until "+date_impression.iat[-1,0].split("T",1)[0],fontsize=15)
    ax.set_ylabel('Chart')
    ax.set_xlabel('Average Percentage and (number of people)')
    ax.legend(labels=labels_Ages,
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    plt.savefig("charts/Men-Age-Impression"+".png",dpi=300)
    print("Men : Age-Impression chart was created!")
    plt.clf()
    
def plot_city(dataframe1,dataframe2):
      #print(dataframe1)
      #print(dataframe2)

      date_content=dataframe1.iloc[:,0:1]
      date_impression = dataframe1.iloc[:,0:1]

      #print(date_content.iat[-1,0])
      sub_content=  dataframe1.iloc[:,1:]
      sub_impression = dataframe2.iloc[:,1:]
      
      top10_content = sub_content.mean().nlargest(10)
      top10_impression = sub_impression.mean().nlargest(10)

      objects_content= top10_content.axes
      
      fig, ax = plt.subplots(figsize=(12, 12))
      top10_content.plot(kind='bar',use_index=True,position=0.8, grid=True,fontsize=8,rot=6,)
      plt.ylabel('People that are talking about the Page',fontsize=15)
      plt.title('Average content activity. Days: '+date_content.iat[0,0].split("T",1)[0]+" until "+date_content.iat[-1,0].split("T",1)[0],fontsize=15)
      plt.savefig("charts/City-Content"+".png",dpi=300)
      print("City-Content Activity chart was created!")
      plt.clf()

      fig, ax = plt.subplots(figsize=(12, 12))
      top10_impression.plot(kind='bar',use_index=True, grid=True,fontsize=8,rot=10,)
      plt.ylabel('People that Page was appeared on their screen',fontsize=15)
      plt.title('Average Impressions. Days :'+date_impression.iat[0,0].split("T",1)[0]+" until "+date_impression.iat[-1,0].split("T",1)[0],fontsize=15)
      plt.savefig("charts/City-Impressions"+".png",dpi=300)
      print("City-Impression chart was created!")
      plt.clf()
      #print(top10_content.values)
      
def plot_country(dataframe):
      date_impression = dataframe.iloc[:,0:1]
      sub_impression = dataframe.iloc[:,1:]
      top10_impression = sub_impression.mean().nlargest(10)

      fig, ax = plt.subplots(figsize=(12, 12))
      top10_impression.plot(kind='bar',use_index=True,position=0.8, grid=True,fontsize=8,rot=6,)
      plt.ylabel('People\'s Countries in which the Page was appeared on their screens',fontsize=15)
      plt.title('Average content activity. Days: '+date_impression.iat[0,0].split("T",1)[0]+" until "+date_impression.iat[-1,0].split("T",1)[0],fontsize=15)
      plt.savefig("charts/Country-Impression"+".png",dpi=300)
      print("Country-Impression chart was created!")
      plt.clf()

def run_charts():

   
      
      xlsxfile_age_content ='excels/Ages-Content.xlsx'
      age_content = pd.read_excel(xlsxfile_age_content)
      plot_ages_content(age_content)

      xlsxfile_age_impression = 'excels/Ages-Impressions.xlsx'
      age_impression = pd.read_excel(xlsxfile_age_impression)
      plot_ages_impressions(age_impression)


      xlsxfile_city_content = 'excels/City-Content.xlsx'
      city_content = pd.read_excel(xlsxfile_city_content)
      xlsxfile_city_impression = 'excels/City-Impression.xlsx'
      city_impression = pd.read_excel(xlsxfile_city_impression)
      plot_city(city_content,city_impression)

      xlsxfile_country_impression = 'excels/Country-Impression.xlsx'
      country_impression= pd.read_excel(xlsxfile_country_impression)
      plot_country(country_impression)

run_charts()