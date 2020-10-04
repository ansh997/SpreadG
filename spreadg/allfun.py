import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# styling plt
plt.rcParams['font.family'] = 'Hevletica'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12

# Set an aspect ratio
width, height = plt.figaspect(1/3)
fig = plt.figure(figsize=(width,height), dpi=400)

# defining api vars
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


def authorize(filename):
    creds = ServiceAccountCredentials.from_json_keyfile_name(filename, scope)
    client = gspread.authorize(creds)
    return client


def dataloader(filename, sheetname):
    client = authorize(filename)
    sheet = client.open(sheetname).sheet1  # Open the spreadhseet
    data = sheet.get_all_records()  # Get a list of all records
    return data

# working with Data

def to_df(data):
    df=pd.DataFrame(data)
    return df

def plotter(df, x, y):
    if x!='timestamp':
        plt.plot(df[x], df['y'])
        # naming the x axis 
        plt.xlabel(x) 
        # naming the y axis 
        plt.ylabel(y) 
        # giving a title to my graph 
        plt.title(f'{x} VS. {y}') 
        # function to show the plot 
        plt.show() 
        plt.savefig('data.pdf')
    else:
        df[x]=pd.to_datetime(df[x], unit='s')
        df = df.set_index(x)

        # plotting the data
        df[y].resample('m').mean().plot()
        # df['average_sales'].resample('w').mean().plot()

        # naming the x axis 
        plt.xlabel(x) 
        # naming the y axis 
        plt.ylabel(y) 
        # giving a title to my graph 
        plt.title(f'{x} VS. {y}') 
        # function to show the plot 
        plt.show() 
        plt.savefig('data.pdf')
