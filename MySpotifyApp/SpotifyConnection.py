import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


username = 12147687832
## test username is 12147687832

SPOTIPY_CLIENT_ID='7372aad238034bcd80dabd1c3925a2d0'
SPOTIPY_CLIENT_SECRET='e690456872084adc93289a2175acd86c'
SPOTIPY_REDIRECT_URI='http://localhost:1410/'

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)
spot = spotipy.Spotify()
userPlaylists = ''
playlists = sp.user_playlists(username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        userPlaylists += "%4d %s\n" % (i + 1 + playlists['offset'], playlist['name'])
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

# print(sp.search(q="green day", limit=20))
# set SPOTIPY_CLIENT_ID='7372aad238034bcd80dabd1c3925a2d0'
# set SPOTIPY_CLIENT_SECRET='e690456872084adc93289a2175acd86c'
# set SPOTIPY_REDIRECT_URI='http://localhost:1410/'
SelectionOptions = ["Artist", "Album", "Track Name", "Genre"]

#def get_username:


def get_artist(artistName):
    result = sp.search(q="Green Day")
    return result
#def get_track:

#def get_album:

#def get_genre:

#def get_playlist:


#def pie_chart:

#def bar_graph:

#def scatter_plot:


