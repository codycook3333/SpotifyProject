from hashlib import new
from unittest import result
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pandastable import *
import pandas as pd
import matplotlib as plt
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
    artistIDList =[]
    while i < 20:
        #get list of recommended artists based off of artist, genre, or track
        artistRecomList.append(recom['tracks'][i]['artists'][0]['name'])
        artistIDList.append(recom['tracks'][i]['artists'][0]['id'])
        #get list of thier popularity
        popRecomList.append(recom['tracks'][i]['popularity'])
        i+=1
    recomDict = {'Artist Name': artistRecomList, 'Popularity': popRecomList}
    recomDF = pd.DataFrame(data=recomDict)
    return recomDF, artistIDList






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
    colNames = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time signature']
    df = pd.DataFrame(data=resultList, index=colNames)
    df.columns=['']
    dfT = df.transpose()
    return df, resultList, dfT


def get_plot_data(artistIDList):
    trackList = []
    bigDF = pd.DataFrame()
    k = 0
    frames = []
    while k < 2:
        artistsAlbums = sp.artist_albums(artistIDList[k])
        albumID = artistsAlbums['items'][0]['id']
        album1 = sp.album_tracks(albumID)
        album1 = album1['items']
        j = 0
        for tracks in album1:
            trackList.append(album1[j]['id'])
            j +=1   
        k += 1
    i = 0
    for ids in trackList:
        df1 = pd.DataFrame()
        df1 = get_audio_features(trackList[i])[2]
        frames.append(df1)
        i += 1

    bigDF = pd.concat(frames)
    # print(bigDF)
    return bigDF
    

# newResults = sp.album_tracks('6BkzuBcjPyjUiLe2OzVHks')
# print(newResults['items'][0]['id'])

# temp track id is 4XpeLct2suqK9hbsIDJQZz

# frames = []
# results = get_audio_features('4XpeLct2suqK9hbsIDJQZz')[2]
# result2 = get_audio_features('4XpeLct2suqK9hbsIDJQZz')[2]
# frames.append(results)
# frames.append(result2)
# results3 = pd.concat(frames)
# print(results3)
# trackList = []
# artistsAlbums = sp.artist_albums('4NGshr0X0WNGCy4emP2O0Z')
# albumID = artistsAlbums['items'][0]['id']
# album1 = sp.album_tracks(albumID)
# album1 = album1['items']
# j = 0
# for i in album1:
#     trackList.append(album1[j]['id'])
#     j +=1
# df1 = pd.DataFrame()
# infoList = []
# i = 0
# for k in trackList:
    
#     if df1.empty == True:
#         df1 = get_audio_features(trackList[i])[0]
#     else:
#         infoList  = get_audio_features(trackList[i])[1]
#         df1.insert(loc = i, column=i, value=infoList)
#     i += 1
# df1T = df1.transpose()
# df1T2 = df1T
# frames = [df1T, df1T2]
# newDF = pd.concat(frames)
# print(newDF)



# Temp album id is 6BkzuBcjPyjUiLe2OzVHks