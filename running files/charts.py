from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates




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
   
    print(top10)
   
    fig, ax = plt.subplots(figsize=(12, 12))
    top10.plot(kind='bar',use_index=True,position=0.8, grid=True,fontsize=8,rot=6,)
    #plt.ylabel('People that are talking about the Page',fontsize=15)
    plt.title('Top 10 Cities with Fans of the Page',fontsize=12)
    plt.ylabel('Chart',fontsize=12)
    plt.savefig("charts_new/City-bar"+".png",dpi=300)
    print("City bar-chart was created!")
    plt.clf()

    top10.plot(kind='pie',autopct='%1.1f%%',textprops=dict(color="black"))
    plt.ylabel('People that are talking about the Page',fontsize=15)
    plt.title('Top 10 Cities with Fans of the Page',fontsize=12)
    plt.savefig("charts_new/City-pie"+".png",dpi=300)
    print("City bar-pie was created!")
    plt.clf()


def main():
    '''
    age_gender = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')
    plot_ages_gender_df(age_gender)
    '''
    city = pd.read_excel('excels/lite/lite-City.xlsx')
    plot_city_country_locale(city,"City")


main()