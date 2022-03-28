import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
username = get_username()


playlists = sp.user_playlists(username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
# export SPOTIPY_CLIENT_ID='7372aad238034bcd80dabd1c3925a2d0'
# export SPOTIPY_CLIENT_SECRET='e690456872084adc93289a2175acd86c'
# export SPOTIPY_REDIRECT_URI='http://localhost:1410/'

#def get_username:


#def get_artist:

#def get_track:

#def get_album:

#def get_genre:

#def get_playlist:


#def pie_chart:

#def bar_graph:

#def scatter_plot:


