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


def print_dataframes_excels(dataframe):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            labels_list = list(dataframe.index)
            rows = dataframe.loc[ [ (' Thessaly, Greece', 'Male'), ('Thessaly, Greece', 'Female') ] ,'Total'   ]
            print(rows)



def main():
    education = pd.read_excel('excels/elstat/formated epipedo ekpaideusis.xlsx')
    print_dataframes_excels(education)






main()