from sys import maxsize
from tkinter import *
from tkinter import ttk
import tkinter as tk
from unittest import result
import SpotifyConnection as SC

#TK_SILENCE_DEPRECATION=1


# sets the username so that we can connect to thier spotify
def set_username():
    SC.username = usernameText.get()
    # print(SC.username)
    SC.connect()

def searchCommand():
    if selectionBox.current() == 0:
        
        searchResults = tk.Text(root)
        searchResults.grid(row=15, column=0, pady=15)
        searchResults.insert('1.0', SC.get_artist(searchText.get()))

root = Tk()
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=100)
root.columnconfigure(2, minsize=100)
root.columnconfigure(3, minsize=100)
usernameText = tk.StringVar()
searchText = tk.StringVar()
selection = tk.StringVar()
frm = ttk.Frame(root, padding=10)

root.geometry("800x800")
frm.grid()
ttk.Label(frm, text="Enter Username to access your Spotify information.").grid(column=0, row=0, padx=5, pady=5)
usernameEntry = ttk.Entry(frm, textvariable=usernameText, show="*").grid(column=1, row=0, padx=5, pady=5)
#usernameEntry.focus()

ttk.Button(frm, text=" Set Username and Connect ", command=set_username).grid(column=2, row=0, padx=5, pady=5)



# this is the dropdown menu to specify what to search for

ttk.Label(frm, text="What are you searching for?", anchor="e").grid(column=0, row=3, padx=5, pady=5)

selectionBox = ttk.Combobox(frm, textvariable=selection, values=SC.SelectionOptions)
selectionBox.grid(column=1, row=3, padx=5, pady=5)
selectionBox.current(0)

ttk.Label(frm, text="Name of what you are searching for", anchor="e").grid(column=0, row=6, padx=5, pady=5)
searchEntry = ttk.Entry(frm, textvariable=searchText).grid(column=1, row=6, padx=5, pady=5)
ttk.Button(frm, text=" Search ", command=searchCommand).grid(column=2, row=6, padx=5, pady=5)


#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=15, row=15)
root.mainloop()

