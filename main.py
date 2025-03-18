from multiprocessing.sharedctypes import Value
from xml.sax.handler import feature_external_ges
from matplotlib.axis import XAxis
import pandas as pd
from matplotlib import pyplot as plt

#Import the required Libraries
from tkinter import *
from tkinter import ttk

# Creating win Tkinter window
win = Tk()
win.geometry("275x175")
 
# Tkinter string variable
# able to store any string value
v = StringVar(win, "1")

# Define a function to get the output for selected option
def selection():
   selected = "You selected the option " + str(radio.get())
   label.config(text=selected)
 
radio = IntVar()
Label(text="Your Favourite programming language:", font=('Aerial 11')).pack()

# Define radiobutton for each options
r1 = Radiobutton(win, text="top 20 selling games in Europe on a bar chart", variable=radio, value=1, command=selection)
r1.pack(anchor=N)

r2 = Radiobutton(win, text="top 20 selling games worldwide on a bar chart", variable=radio, value=2, command=selection)
r2.pack(anchor=N)

r3 = Radiobutton(win, text="top selling genres in Europe on a pie chart", variable=radio, value=3, command=selection)
r3.pack(anchor=N)

r4 = Radiobutton(win, text="top 20 selling games world wide on a histogram", variable=radio, value=4, command=selection)
r4.pack(anchor=N)

r5 = Radiobutton(win, text="top game sold on each platform as a list", variable=radio, value=5, command=selection)
r5.pack(anchor=N)
# Define a label widget
label = Label(win)
label.pack()

win.mainloop()

if str(radio.get())=="1":
   #Task1: Top 20 selling games in EU
   df = pd.read_csv('vgsales_data.csv')

   #Remove columns not needed
   df.drop(['Platform'], axis=1, inplace=True)
   df.drop(['Year'], axis=1, inplace=True)
   df.drop(['Genre'], axis=1, inplace=True)
   df.drop(['Publisher'], axis=1, inplace=True)
   df.drop(['NA_Sales'], axis=1, inplace=True)
   df.drop(['JP_Sales'], axis=1, inplace=True)
   df.drop(['Other_Sales'], axis=1, inplace=True)

   #Set the index
   df.set_index('Name', inplace=True)

   #Group the data by Name
   df5 = df.groupby(['Name'] ).sum()
   df5 = (df.head(20))
   
   #Group up EU_Sales
   df5EUS = df.groupby(["EU_Sales"] ).sum()
   df5EUS = (df.head(20))

   #Now sort the data by EU_Sales
   sorted_dfq5 = df5.sort_values(by='EU_Sales', ascending = False, inplace = True)

   #print out data to check it is correct
   print (df5)

   #Create chart
   df5.plot.bar(stacked = True)
   plt.title("Top 20 Game Sales in Europe")
   plt.show()

elif str(radio.get())=="2":
   #Task2: Top 20 selling games by world wide
   df = pd.read_csv('vgsales_data.csv')

   #Remove columns not needed
   df.drop(['Platform'], axis=1, inplace=True)
   df.drop(['Year'], axis=1, inplace=True)
   df.drop(['Genre'], axis=1, inplace=True)
   df.drop(['Publisher'], axis=1, inplace=True)

   #add new column for ww sales
   df.loc[:,'ww_sales'] = df.sum(axis=1)

   #Set the index
   df.set_index('Name', inplace=True)

   #Group the data by Name
   df5 = df.groupby(['Name'] ).sum()
   df5 = (df.head(20))

   #Now sort the data by ww_sales
   sorted_dfq5 = df5.sort_values(by='ww_sales', ascending = False, inplace = True)


   #print out data to check it is correct
   print (df5)

   #Remember to remove ww_sales column before chart creation
   df5.drop(['ww_sales'], axis=1, inplace=True)

   #Create chart
   df5.plot.bar(stacked = True)
   plt.xticks(rotation = 90)
   plt.title("Top 20 Sales Worldwide")
   plt.show()

elif str(radio.get())=="3":
   #Task3: Top 20 selling genres in EU as a pie chart
   df = pd.read_csv('vgsales_data.csv')

   #Remove columns not needed
   df.drop(['Name'], axis=1, inplace=True)
   df.drop(['Platform'], axis=1, inplace=True)
   df.drop(['Year'], axis=1, inplace=True)
   df.drop(['Publisher'], axis=1, inplace=True)
   df.drop(['NA_Sales'], axis=1, inplace=True)
   df.drop(['JP_Sales'], axis=1, inplace=True)
   df.drop(['Other_Sales'], axis=1, inplace=True)

   #Set the index
   df.set_index('Genre', inplace=True)

   #Group the data by Genre
   df5 = df.groupby(['Genre'] ).sum()
   df5 = (df.head(20))
   
   #Group up EU_Sales
   df5EUS = df.groupby(["EU_Sales"] ).sum()
   df5EUS = (df.head(20))

   #Now sort the data by EU_Sales
   sorted_dfq5 = df5.sort_values(by='EU_Sales', ascending = False, inplace = True)

   #print out data to check it is correct
   print (df5)

   #Create chart
   df5.plot.pie(subplots = True)
   plt.title("Top 20 Game Sales in Europe")
   plt.show()

elif str(radio.get())=="4":
   #Task2: Top selling genres world wide on a histogram
   df = pd.read_csv('vgsales_data.csv')

   #Remove columns not needed
   df.drop(['Name'], axis=1, inplace=True)
   df.drop(['Platform'], axis=1, inplace=True)
   df.drop(['Year'], axis=1, inplace=True)
   df.drop(['Publisher'], axis=1, inplace=True)

   #Set the index
   df.set_index('Genre', inplace=True)

   #Group the data by Genre
   df5 = df.groupby(['Genre']).sum()
   df5 = (df.head(20))

   #print out data to check it is correct
   print (df5)

   X = df.groupby(["NA_Sales"]).sum()
   X = (X,df.groupby(["EU_Sales"]).sum())
   X = (X,df.groupby(["JP_Sales"]).sum())
   X = (X,df.groupby(["Other_Sales"]).sum())

   #Create chart
   df5.plot.hist()
   
   plt.xlabel("Sales")
   plt.ylabel("Frequency")
   plt.title("Top 20 Sales Worldwide")
   plt.show()

elif str(radio.get())=="5":
   #Task5: Top selling games by platform
   df = pd.read_csv('vgsales_data.csv')

   #Remove columns not needed
   df.drop(['Year'], axis=1, inplace=True)
   df.drop(['Genre'], axis=1, inplace=True)
   df.drop(['Publisher'], axis=1, inplace=True)

   #add new column for ww sales
   df.loc[:,'ww_sales'] = df.sum(axis=1)

   #Set the index
   df.set_index('Platform', inplace=True)

   #Group the data by Genre
   df5 = df.groupby(['Platform'] ).sum()
   df5 = (df.head(20))

   #Now sort the data by ww_sales
   sorted_dfq5 = df5.sort_values(by='ww_sales', ascending = False, inplace = True)


   #print out data to check it is correct
   print (df5)

   #Remember to remove ww_sales column before chart creation
   df5.drop(['ww_sales'], axis=1, inplace=True)

   #Create chart
   df5.plot.bar(stacked = True)
   plt.title("Sales by Platform Worldwide")
   plt.show()