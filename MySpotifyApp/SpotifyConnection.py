from hashlib import new
from unittest import result
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pandastable import *
import pandas as pd
import matplotlib as plt


# ID's required to preform searches

SPOTIPY_CLIENT_ID='7372aad238034bcd80dabd1c3925a2d0'
SPOTIPY_CLIENT_SECRET='e690456872084adc93289a2175acd86c'
SPOTIPY_REDIRECT_URI='http://localhost:1410/'


# Authentication for the searches

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)


# List of strings for dropdown menu options

SelectionOptions = ["Artist", "Track Name", "Genre"]
plotOptions = ['Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Time Signature']


# Get artist function for the artist search

def get_artist(artistName):
    result = sp.search(q='artist:' + artistName, type='artist')
    items=result['artists']['items']
    if len(items) > 0:
        artist = items[0]
    if result['artists']['items'] == []:
        result = "No results found"
        return result
    newResults = sp.artist(artist['id'])
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


# Recommendation function

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


# Get track information function

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


# Get Genre results function

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


# Get audio features function for the plots

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


# This sorts the data into a data frame so that we can Plot it

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

    return bigDF
   