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


SelectionOptions = ["Artist", "Track Name", "Genre"]
plotOptions = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']


def get_artist(artistName):
    result = sp.search(q='artist:' + artistName, type='artist')
    items=result['artists']['items']
    if len(items) > 0:
        artist = items[0]
    if result['artists']['items'] == []:
        result = "No results found"
        return result
    newResults = sp.artist(artist['id'])
    # d = {'Artist Name': [newResults['name']], 'Total Followers': [newResults['followers']['total']], 'Genres': [newResults['genres']], 'ID': [newResults['id']], 'Popularity': [newResults['popularity']]}
    # df = pd.DataFrame(data=d)
    filteredResults = []
    filteredResults.append(newResults['name'])
    filteredResults.append(newResults['followers']['total'])
    filteredResults.append(newResults['genres'][:3])
    filteredResults.append(newResults['id'])
    filteredResults.append(newResults['popularity'])
    colNames = []
    colNames = ['Artist Name: ', 'Total Followers: ', 'Genres: ', 'ID: ', 'Popularity: ']
    df = pd.DataFrame(data=filteredResults, index=colNames)
    df.columns = ['']
    return df

def recommendation(info, boxPlace):
    if boxPlace == 0:    
        artistSearch = sp.search(q='artist:' + info, type='artist', limit=1)
        artistItems=artistSearch['artists']['items']
        if len(artistItems) > 0:
            artist = artistItems[0]
        if artistSearch['artists']['items'] == []:
            result = "No results found"
            return result
    
    elif boxPlace ==1:
        #do some stuff
        result = sp.search(q='track:' + info, type='track')
        items=result['tracks']['items']
        if len(items) > 0:
            items = items[0]
        if result['tracks']['items'] == []:
            result = "No results found"
            return result
        artist = sp.artist(items['artists'][0]['id'])
        if artist == []:
            result = "No results found"
            return result
        
    else: 
        artist = get_genre(info)[1][0]['artists'][0]

    artistSeed = []
    artistSeed.append(artist['id'])
    
    if boxPlace ==1 or boxPlace==0:
        genreSeed = artist['genres'][:2]
    
    else: 
        genreSeed = info
    
    trackSeed = []
    recom = sp.recommendations(seed_artists=artistSeed, seed_genres=genreSeed, seed_tracks=trackSeed)
    i = 0 
    artistRecomList = []
    popRecomList = []
    while i < 20:
        #get list of recommended artists based off of artist, genre, or track
        artistRecomList.append(recom['tracks'][i]['artists'][0]['name'])
        #get list of thier popularity
        popRecomList.append(recom['tracks'][i]['popularity'])
        i+=1
    recomDict = {'Artist Name': artistRecomList, 'Popularity': popRecomList}
    recomDF = pd.DataFrame(data=recomDict)
    return recomDF, artistRecomList






def get_track(trackName):
    result = sp.search(q='track:' + trackName, type='track')
    items=result['tracks']['items']
    if len(items) > 0:
        items = items[0]
    if result['tracks']['items'] == []:
        result = "No results found"
        return result
    genreSearch = sp.artist(items['artists'][0]['id'])
    genre = genreSearch['genres']
    filteredResults = []
    filteredResults.append(items['name'])
    filteredResults.append(items['artists'][0]['name'])
    filteredResults.append(items['popularity'])
    filteredResults.append(genre[0:3])
    colNames = []
    colNames = ['Track Name', 'Artist Name: ', 'Popularity: ', 'Genres: ']
    df = pd.DataFrame(data=filteredResults, index=colNames)
    df.columns = ['']
    return df

def get_genre(genre):
    result = sp.search(q='genre:' + genre)
    items=result['tracks']['items']
    tracks = ""
    i = 0
    if result['tracks']['items'] == []:
        result = "No results found"
        return result
    else:
        while i < 10:
            tracks += (items[i]['name'] + ' - ' + items[i]['artists'][0]['name'] + '\n')
            i+=1
        return tracks, items

def get_audio_features(track_id):
    result = sp.audio_features(track_id)
    resultList = []
    resultList.append(result[0]['danceability'])
    resultList.append(result[0]['energy'])
    resultList.append(result[0]['loudness'])
    resultList.append(result[0]['speechiness'])
    resultList.append(result[0]['acousticness'])
    resultList.append(result[0]['instrumentalness'])
    resultList.append(result[0]['liveness'])
    resultList.append(result[0]['valence'])
    resultList.append(result[0]['tempo'])
    resultList.append(result[0]['time_signature'])
    colNames = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']
    df = pd.DataFrame(data=resultList, index=colNames)
    df.columns=['']
    return df


# artistSeed = []
# artistSeed.append('7oPftvlwr6VrsViSDV7fJY')
# genreSeed = 'punk'
# trackSeed = []
# recom = sp.recommendations(seed_artists=artistSeed, seed_genres=genreSeed, seed_tracks=trackSeed)
# print(recom)

#def bar_graph:

#def scatter_plot:


