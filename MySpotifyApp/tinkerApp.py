from cgitb import text
from sys import maxsize
from tkinter import *
from tkinter import ttk
import tkinter as tk
import SpotifyConnection as SC
from pandastable import Table

#TK_SILENCE_DEPRECATION=1


# sets the username so that we can connect to thier spotify
def set_username():
    SC.username = usernameText.get()
    # print(SC.username)
    SC.connect()


def searchCommand():
    searchResults = tk.Text(can)
    searchResults.config(height=7)
    searchResults.place(relx=.5, rely=.5, anchor=CENTER)
    if selectionBox.current() == 0:
        searchResults.insert('1.0', SC.get_artist(searchText.get()))
        # searchResults= tk.Label(frm2, text=SC.get_artist(searchText.get())).grid(row=1, column=0, pady=15, columnspan=6)
        # df = SC.get_artist(searchText.get())
        # artName = ttk.Label(frm2, text=df.iloc[0]).grid(row=1, column=0, pady=15)
    # elif selectionBox.current() == 1:
    #     searchResults.insert('1.0', SC.get_artist(searchText.get()))

    # elif selectionBox.current() == 2:
    #     searchResults.insert('1.0', SC.get_artist(searchText.get()))

    # elif selectionBox.current() == 3:
    #     searchResults.insert('1.0', SC.get_artist(searchText.get()))
    recommendArtist()

def recommendArtist():
    recommendBox = tk.Text(can2)
    recommendBox.config(height=12)
    recommendBox.place(relx=.5, rely=.5, anchor=CENTER)
    recommendBox.insert('1.0', 'Other users also liked: \n\n ' + SC.recommendation(searchText.get(), selectionBox.current()))


root = Tk()
#------------------------------------------------------------------------------------------------------------------
# root.columnconfigure(0, minsize=1000)
# root.columnconfigure(1, minsize=100)
# root.columnconfigure(2, minsize=100)
# root.columnconfigure(3, minsize=100)
usernameText = tk.StringVar()
searchText = tk.StringVar()
selection = tk.StringVar()
frm = Canvas(root, bg='red', height=200, width=800)
frm.place(relx=0.5, rely=0.2, anchor=CENTER)
can = Canvas(root, bg='green', height=200, width=800)
can.place(relx=0.5, rely=0.5, anchor=CENTER)
root.geometry("1000x800")
can2 = Canvas(root, bg='blue', height=200, width=800)
can2.place(relx=0.5, rely=0.8, anchor=CENTER)
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


#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=15, row=15)
#----------------------------------------------------------------------------------------------------------------------
root.mainloop()

