from cgitb import text
from sys import maxsize
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
from turtle import width
import SpotifyConnection as SC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#TK_SILENCE_DEPRECATION=1


# # sets the username so that we can connect to thier spotify
# def set_username():
#     SC.username = usernameText.get()
#     # print(SC.username)
#     SC.connect()
artistIDList = []
df = pd.DataFrame
def searchCommand():
    ttk.Label(resultLabel, text="Search Results", font=('Times', 30)).place(relx=0.5, rely=0.5, anchor=CENTER)
    ttk.Label(recomLabel, text="Recommendations", font=('Times', 30)).place(relx=0.5, rely=0.5, anchor=CENTER)
    searchResults = tk.Text(can)
    searchResults.config(height=7, width=62)
    searchResults.place(relx=.5, rely=0.5, anchor=CENTER)
    if selectionBox.current() == 0:
        searchResults.insert('1.0', SC.get_artist(searchText.get()))
        
    elif selectionBox.current() == 1:
        searchResults.insert('1.0', SC.get_track(searchText.get()))

    elif selectionBox.current() == 2:
        searchResults.insert('1.0', SC.get_genre(searchText.get())[0])

    
    recommendArtist(searchText.get(), selectionBox.current())

def recommendArtist(text, boxPos):
    recommendBox = tk.Text(can2)
    recommendBox.config(height=12, width=45)
    recommendBox.place(relx=.5, rely=.5, anchor=CENTER)
    results = SC.recommendation(text, boxPos)
    recommendBox.insert('1.0', results[0])
    global artistIDList 
    artistIDList = results[1]
    global df
    df = SC.get_plot_data(artistIDList)
    
    # ______________________________________     print(df.iloc[:, 0])

def plotFunction():  
    global df
    if fig.axes:
        fig.delaxes(fig.axes[0])

    columnPos = plotSelectionBox1.current()
    
    ydata = df.iloc[:, columnPos]
    xdata = list(np.arange(0,len(ydata),1))
    xlim = len(ydata) + 5
    ax1 = fig.add_subplot(111)
    ax1.scatter(xdata, ydata)
    ax1.set_xlim([0,xlim])
    ax1.set_ylim([0,1])
    if columnPos == 0 or columnPos == 1 or columnPos == 7:
        ax1.set_ylim([0,1])
    elif columnPos == 2:
        ax1.set_ylim([-10,0])
    elif columnPos == 3 or columnPos == 4:
        ax1.set_ylim([0,0.5])
    elif columnPos == 5:
        ax1.set_ylim([0,0.02])
    elif columnPos == 6:
        ax1.set_ylim([0,1])
    elif columnPos == 8:
        ax1.set_ylim([50,220])
    elif columnPos == 9:
        ax1.set_ylim([0,10])
    canvas.draw()
    canvas.get_tk_widget().pack(side= 'bottom', anchor=SE)





root = Tk()
#------------------------------------------------------------------------------------------------------------------

usernameText = tk.StringVar()
searchText = tk.StringVar()
selection = tk.StringVar()
selection2 = tk.StringVar()
selection3 = tk.StringVar()
root.geometry("1200x800")
titleLabel = Canvas(root,  height = 50 , width=500)
titleLabel.place(relx = 0, rely=0.05, anchor=W)

frm = Canvas(root, height=175, width=500)
frm.place(relx=0, rely=0.22, anchor=W)

resultLabel = Canvas(root, height = 50 , width=500)
resultLabel.place(relx = 0, rely=0.39, anchor=W)

can = Canvas(root, height=200, width=500)
can.place(relx=0, rely=0.55, anchor=W)

recomLabel = Canvas(root, height = 50 , width=500)
recomLabel.place(relx = 0, rely=0.69, anchor=W)

can2 = Canvas(root, height=200, width=500)
can2.place(relx=0, rely=0.85, anchor=W)

can3 = Canvas(root, height=250, width=600)
can3.place(relx=1, rely=.2, anchor=E)
#frm.grid()
#frm2.grid()
fig = Figure(figsize = (5, 5), dpi =100)

canvas = FigureCanvasTkAgg(fig, master=root)
# Username entry for persoanl user playlists

# ttk.Label(frm, text="Enter Username to access your Spotify information.").grid(column=0, row=0, padx=5, pady=5)
# usernameEntry = ttk.Entry(frm, textvariable=usernameText, show="*").grid(column=1, row=0, padx=5, pady=5)
# ttk.Button(frm, text=" Set Username and Connect ", command=set_username).grid(column=2, row=0, padx=5, pady=5)


ttk.Label(titleLabel, text="Song Data Visualization", font=('Times', 30)).place(relx=0.5, rely=0.5, anchor=CENTER)
# ttk.Label(resultLabel, text="Search Results", font=('Times', 30)).place(relx=0.5, rely=0.5, anchor=CENTER)
# ttk.Label(recomLabel, text="Recommendations", font=('Times', 30)).place(relx=0.5, rely=0.5, anchor=CENTER)

# Dropdown menu to specify what to search for

ttk.Label(frm, text="What are you searching for?").place(relx=0.2, rely=0.3, anchor=CENTER)
selectionBox = ttk.Combobox(frm, textvariable=selection, values=SC.SelectionOptions)
selectionBox.place(relx=0.8, rely=0.3, anchor=CENTER)  
selectionBox.current(0)

# Search box to enter in your search results

ttk.Label(frm, text="Name of what you are searching for").place(relx=0.2, rely=0.6, anchor=CENTER)  
searchEntry = ttk.Entry(frm, textvariable=searchText).place(relx=0.8, rely=0.6, anchor=CENTER) 
ttk.Button(frm, text=" Search ", command=searchCommand).place(relx=0.5, rely=0.8, anchor=CENTER) 

# Buttons for plots
ttk.Button(can3, text=" Plot ", command=plotFunction).place(relx=0.4, rely=0.3, anchor=CENTER) 
# ttk.Button(can3, text=" Plot ", command=searchCommand).place(relx=0.3, rely=0.1, anchor=CENTER)
# ttk.Button(can3, text=" Histogram ", command=searchCommand).place(relx=0.5, rely=0.1, anchor=CENTER)
# ttk.Button(can3, text=" Plot ", command=searchCommand).place(relx=0.7, rely=0.1, anchor=CENTER)
# ttk.Button(can3, text=" Box Plot ", command=searchCommand).place(relx=0.9, rely=0.1, anchor=CENTER)

# Menu to choose what to plot
ttk.Label(can3, text="Value to Plot ").place(relx=0.1, rely=0.1, anchor=CENTER)
plotSelectionBox1 = ttk.Combobox(can3, textvariable=selection2, values=SC.plotOptions)
plotSelectionBox1.place(relx=0.3, rely=0.1, anchor=CENTER)
plotSelectionBox1.current(0)
# ttk.Label(can3, text="Y Value = ").place(relx=0.62, rely=0.3, anchor=CENTER)
# plotSelectionBox2 = ttk.Combobox(can3, textvariable=selection3, values=SC.plotOptions)
# plotSelectionBox2.place(relx=0.8, rely=0.3, anchor=CENTER)
# plotSelectionBox2.current(0)


# Plot location


#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=15, row=15)
#----------------------------------------------------------------------------------------------------------------------
root.mainloop()

