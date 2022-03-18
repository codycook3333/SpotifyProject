import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
username = '12147687832'


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
