from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

def plot_dataframe(dataframe):   
    labels=list(dataframe.columns.values)
    num=len(labels)
    ax = plt.gca()
    ax.xaxis.set_minor_formatter(dates.DateFormatter('d/%m/%Y'))
    print(num)
    print(dataframe)
    print(type(dataframe['Date']))
    #my_dates = dataframe["Date"].tolist()

   
    #xdates = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in my_dates]
    
    if num==4:
        dataframe.plot(kind='line',x=labels[0],y=[labels[1],labels[2],labels[3]],ax=ax)
        plt.title(labels[0]+"-"+labels[1]+"-"+labels[2]+"-"+labels[3])
        plt.savefig("charts/"+labels[0]+"-"+labels[1]+"-"+labels[2]+"-"+labels[3]+".png")
    else:
        dataframe.plot(kind='line',x=labels[0],y=[labels[1],labels[2]],ax=ax)
        plt.title(labels[0]+"-"+labels[1]+"-"+labels[2])
        plt.savefig("charts/"+labels[0]+"-"+labels[1]+"-"+labels[2]+".png")
    #dataframe.plot(kind='line',x=labels[0],y=labels[2], color='red', ax=ax)
    
    
    print("successfully ploted")
    plt.clf()
    

excel_file1 = '/Users/giorgosandreou/Documents/Visual Studio/Facebook data mining/excels/Fan-NewLikes.xlsx'
fan_likes = pd.read_excel(excel_file1)

excel_file2 = '/Users/giorgosandreou/Documents/Visual Studio/Facebook data mining/excels/Impression-View-Engaged.xlsx'
impression_view = pd.read_excel(excel_file2)

plot_dataframe(impression_view)
plot_dataframe(fan_likes)



