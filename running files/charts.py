from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import plotly.graph_objs as go
import plotly.io as pio




def plot_ages_gender_df(dataframe):
    labels=list(dataframe.columns.values)
    print(labels)
    num=len(labels)
    ax = plt.gca()
    dataframe.plot(kind='line',x=labels[0],y=[labels[1],labels[2],labels[3],labels[4],labels[5],labels[6],labels[7]],ax=ax)
    plt.title("Women:"+"Age Fans Chart")
    ax.grid()
    ax.legend(
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(0,0,1,1))
    plt.savefig("charts_new/"+"Age-Women"+".png",dpi=300)
    print("Age-Women successfully ploted")
    plt.clf()

    ax = plt.gca()
    dataframe.plot(kind='line',x=labels[0],y=[labels[8],labels[9],labels[10],labels[11],labels[12],labels[13],labels[14]],ax=ax)
    plt.title("Men:"+"Age Fans Chart")
    ax.grid()
    ax.legend(
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(0,0,1,1))
    plt.savefig("charts_new/"+"Age-Men"+".png",dpi=300)
    print("Age-Men successfully ploted")
    plt.clf()

def plot_city_country_locale(dataframe,typpe):
      labels=list(dataframe.columns.values)
      date=labels[0]

      sub_df= dataframe.iloc[:,1:]
      top10 = sub_df.mean().nlargest(10)
      
      top10df = top10.to_frame()
      top10df= top10df.T 
      
      #print(regionDf)

      '''
      FAILED TRY FOR DOUBLE DONUT CHART
      labels_outer = labels
      labels_inner = list(regionDf.columns.values)
      outer_values = top10df
      inner_values = regionDf


      trace1 = go.Pie(
      hole=0.5,
      sort=False,
      direction='clockwise',
      domain={'x': [0.15, 0.85], 'y': [0.15, 0.85]},
      values=inner_values,
      labels=labels_inner,
      textinfo='label',
      textposition='inside',
      marker={'line': {'color': 'white', 'width': 1}}
      )

      trace2 = go.Pie(
      hole=0.7,
      sort=False,
      direction='clockwise',
      values=outer_values,
      labels=labels_outer,
      textinfo='label',
      textposition='outside',
      marker={'colors': ['green', 'red', 'blue'],
                  'line': {'color': 'white', 'width': 1}}
      )

      fig = go.FigureWidget(data=[trace1, trace2])
      pio.write_image(fig, 'charts_new/fig1.png')
      #fig.savefig("charts_new/region-pie"+".png",dpi=300)
      '''

      
      fig, ax = plt.subplots(figsize=(12, 12))
      top10.plot(kind='bar',use_index=True,position=0.8, grid=True,fontsize=8,rot=6,)
     
      plt.title('Top 10 '+typpe+' with Fans of the Page',fontsize=12)
      plt.ylabel('Chart',fontsize=12)
      plt.savefig("charts_new/"+typpe+"-bar"+".png",dpi=300)
      print(typpe+" bar-chart was created!")
      plt.clf()

      fig, ax = plt.subplots(figsize=(12, 12))
      top10.plot(kind='pie',autopct='%1.1f%%',textprops=dict(color="black"))
      plt.ylabel('',fontsize=15)
      #ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True)
      plt.title('Top 10 '+typpe+' with Fans of the Page',fontsize=12)
      plt.savefig("charts_new/"+typpe+"-pie"+".png",dpi=300)
      print(typpe+" pie-chart was created!")
      plt.clf()
      
      if typpe == "City":
            col_val = list(top10df.columns.values)
            col_val = [item.split(",",1)[1] for item in col_val]
            
            col_val=set(col_val) #list with different region names
            temp_dict = {}
            for item in col_val:
                  value=0
                  for col in top10df: 
                        if item in col :
                              value = value + top10df[col].sum()
                  #print("region: "+str(item)+" "+str(value))
                  temp_dict.update({item:value})
                  
            regionDf = pd.DataFrame()
            regionDf = regionDf.from_dict(temp_dict,orient='index')


            fig, ax = plt.subplots(figsize=(12, 12))
            regionDf.plot(kind='pie',autopct='%1.1f%%',textprops=dict(color="black"),subplots=True)
            plt.ylabel('',fontsize=15)
            plt.legend().set_visible(False)
            plt.title('Top 10 '+typpe+' with Fans of the Page',fontsize=12)
            plt.savefig("charts_new/"+typpe+"Region-pie"+".png",dpi=300)
            print(typpe+" Region pie-chart was created!")
            plt.clf()
            
            fig, ax = plt.subplots(figsize=(12, 12))
            regionDf.plot(kind='bar',use_index=True,position=0.8, grid=True,fontsize=8,rot=6,)
            plt.title('Top 10 '+typpe+' with Fans of the Page',fontsize=12)
            plt.ylabel('Chart',fontsize=12)
            plt.savefig("charts_new/"+typpe+"Region-bar"+".png",dpi=300)
            print(typpe+" Region bar-chart was created!")
            plt.clf()


def plot_page_info_page_post(dataframe,typpe):
      '''
      with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(dataframe)
      '''
      labels=list(dataframe.columns.values)
      #print(labels)
      num=len(labels)
      ax = plt.gca()
      dataframe.plot(kind='line',x=labels[0],y=[labels[1],labels[2],labels[3],labels[4],labels[5],labels[6]],ax=ax)
      plt.title(typpe)
      plt.grid()
      box = ax.get_position()
      ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
      ax.legend(
            title=typpe+" Categories",
            loc='center left', bbox_to_anchor=(1, 0.5),
            prop={'size': 4})
      plt.savefig("charts_new/"+typpe+".png",dpi=300)
      print(typpe+" successfully ploted")
      plt.clf()


def main():
      '''
      age_gender = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')
      plot_ages_gender_df(age_gender)

      city = pd.read_excel('excels/lite/lite-City.xlsx')
      plot_city_country_locale(city,"City")

      country = pd.read_excel('excels/lite/lite-Country.xlsx')
      plot_city_country_locale(country,"Country")

      locale = pd.read_excel('excels/lite/lite-Locale.xlsx')
      plot_city_country_locale(locale,"Locale")
      '''

      page_info = pd.read_excel('excels/lite/lite-Page-Info.xlsx')
      plot_page_info(page_info,"Page Info Statistics")

      page_post = pd.read_excel('excels/lite/lite-Page-Post.xlsx')
      plot_page_info(page_post,"Page Post Statistics")


main()
