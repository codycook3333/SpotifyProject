from cgitb import text
from sys import maxsize
from tkinter import *
from tkinter import ttk
import tkinter as tk
from turtle import width
import SpotifyConnection as SC
from pandastable import Table

#TK_SILENCE_DEPRECATION=1


# # sets the username so that we can connect to thier spotify
# def set_username():
#     SC.username = usernameText.get()
#     # print(SC.username)
#     SC.connect()


def searchCommand():
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
    recommendBox.config(height=12, width=35)
    recommendBox.place(relx=.5, rely=.5, anchor=CENTER)
    recommendBox.insert('1.0', SC.recommendation(text, boxPos)[0])


root = Tk()
#------------------------------------------------------------------------------------------------------------------

usernameText = tk.StringVar()
searchText = tk.StringVar()
selection = tk.StringVar()
selection2 = tk.StringVar()
selection3 = tk.StringVar()
frm = Canvas(root, bg='red', height=200, width=500)
frm.place(relx=0, rely=0.2, anchor=W)
can = Canvas(root, bg='green', height=200, width=600)
can.place(relx=1, rely=0.2, anchor=E)
root.geometry("1200x800")
can2 = Canvas(root, bg='blue', height=200, width=500)
can2.place(relx=0, rely=0.5, anchor=W)
can3 = Canvas(root, bg='black', height=500, width=600)
can3.place(relx=1, rely=0.66, anchor=E)
#frm.grid()
#frm2.grid()

# Username entry for persoanl user playlists

# ttk.Label(frm, text="Enter Username to access your Spotify information.").grid(column=0, row=0, padx=5, pady=5)
# usernameEntry = ttk.Entry(frm, textvariable=usernameText, show="*").grid(column=1, row=0, padx=5, pady=5)
# ttk.Button(frm, text=" Set Username and Connect ", command=set_username).grid(column=2, row=0, padx=5, pady=5)



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
ttk.Button(can3, text=" Plot ", command=searchCommand).place(relx=0.1, rely=0.05, anchor=CENTER) 
ttk.Button(can3, text=" Plot ", command=searchCommand).place(relx=0.3, rely=0.05, anchor=CENTER)
ttk.Button(can3, text=" Plot ", command=searchCommand).place(relx=0.5, rely=0.05, anchor=CENTER)
ttk.Button(can3, text=" Plot ", command=searchCommand).place(relx=0.7, rely=0.05, anchor=CENTER)
ttk.Button(can3, text=" Plot ", command=searchCommand).place(relx=0.9, rely=0.05, anchor=CENTER)

# Menu to choose what to plot
ttk.Label(can3, text="X Value = ").place(relx=0.12, rely=0.15, anchor=CENTER)
plotSelectionBox1 = ttk.Combobox(can3, textvariable=selection2, values=SC.plotOptions)
plotSelectionBox1.place(relx=0.3, rely=0.15, anchor=CENTER)
plotSelectionBox1.current(0)
ttk.Label(can3, text="Y Value = ").place(relx=0.62, rely=0.15, anchor=CENTER)
plotSelectionBox2 = ttk.Combobox(can3, textvariable=selection3, values=SC.plotOptions)
plotSelectionBox2.place(relx=0.8, rely=0.15, anchor=CENTER)
plotSelectionBox2.current(0)

#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=15, row=15)
#----------------------------------------------------------------------------------------------------------------------
root.mainloop()

