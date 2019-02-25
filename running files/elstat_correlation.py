from openpyxl import load_workbook
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import plotly.graph_objs as go
import plotly.io as pio


def print_dataframes_excels(filename):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(filename)




def main():
    education = pd.read_excel('excels/elstat/formated epipedo ekpaideusis.xlsx')






main()