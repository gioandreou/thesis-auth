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



def main():

    age_gender = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')
    plot_ages_gender_df(age_gender)

main()