import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pandastable import *
import pandas as pd

username = 12147687832
## test username is 12147687832

SPOTIPY_CLIENT_ID='7372aad238034bcd80dabd1c3925a2d0'
SPOTIPY_CLIENT_SECRET='e690456872084adc93289a2175acd86c'
SPOTIPY_REDIRECT_URI='http://localhost:1410/'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
userPlaylists = ''
playlists = sp.user_playlists(username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        userPlaylists += "%4d %s\n" % (i + 1 + playlists['offset'], playlist['name'])
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
#print(userPlaylists)

SelectionOptions = ["Artist", "Album", "Track Name", "Genre"]

#def get_username:


def get_artist(artistName):
    result = sp.search(q='artist:' + artistName, type='artist')
    items=result['artists']['items']
    if len(items) > 0:
        artist = items[0]
    newResults = sp.artist(artist['id'])
    # d = {'Artist Name': [newResults['name']], 'Total Followers': [newResults['followers']['total']], 'Genres': [newResults['genres']], 'ID': [newResults['id']], 'Popularity': [newResults['popularity']]}
    # df = pd.DataFrame(data=d)
    filteredResults = []
    filteredResults.append(newResults['name'])
    filteredResults.append(newResults['followers']['total'])
    filteredResults.append(newResults['genres'])
    filteredResults.append(newResults['id'])
    filteredResults.append(newResults['popularity'])
    colNames = []
    colNames = ['Artist Name: ', 'Total Followers: ', 'Genres: ', 'ID: ', 'Popularity: ']
    df = pd.DataFrame(data=filteredResults, index=colNames)
    df.columns = ['']
    return df

    

def recommendation(info, boxPlace):
    if boxPlace == 0:
        # we need to find the Genre of the artist
        result = sp.search(q='artist:' + info, type='artist')
        items=result['artists']['items']
        if len(items) > 0:
            artist = items[0]
        newResults = sp.artist(artist['id'])
        artist_id = newResults['id']

    elif boxPlace ==1:
        #we need to find the Artist of the Album
        # We first need the album id
        allinfo = sp.search(q='album:'+ info, type='album')
        albumID = allinfo['albums']['items'][0]['id']
        #then we use that to get the artist id 
        result = sp.album(albumID)
        artist_id = result['artists'][0]['id']
        

    # elif boxPlace == 2:
    #     # we need to find the Artist id of the track name
        
        

    # # #else:
    # #     # we are already given the Genre so begin the search.
    # return sp.artist_related_artists(artist_id)
    # get_genre()

 
# result = sp.search(q='track:'+ 'Given Up', type='track')


# print(result)
# Temp artist id 4uG8q3GPuWHQlRbswMIRS6

#def get_track:

#def get_album:

#def get_genre:

#def get_playlist:


#def pie_chart:

#def bar_graph:

#def scatter_plot:


