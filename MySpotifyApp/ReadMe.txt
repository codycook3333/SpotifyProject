### This file is to explain the functions within the SpotifyConnection.py file and thier purposes/what they do.

get_artist function: 
This function takes the user input (if the artist search drop down was selected)
and returns a data frame of pre-selected options. We do a specific artist search 
here because we only want artists of that name, nothing else. Because the amount 
of data is large, we return the first option (as it is most likely correct) then 
grabs that artists name, total followers, their top 3 genres of thier songs, the 
artists ID and the popularity of the artist. 

recommendation function: 
This function does a recommendation search depending on the dropdown selection 
(artist, track, or genre). We also do a specific search because we care about the 
accuracy of the search for the best results. The recommendation search is complex, 
so we need multiple variables. First we need the artist id or a list of artists ids. 
Depending on the search that was done, the artist ID will be found and used. Then 
we find the genre/s of the music and input that into the search. Track list we can use 
blank under the assumption that most artists stick to a set of genres. They usually 
dont make large leaps in music (such as Death Metal to Country) so the track info is 
unimportant. Once we ahve the results of the search we take the top 20 and just grab
the Artist Name and the popularity. Popularity on this scale is based off of albums and 
not of the artists themselves as Artists genre's can slightly change.

get_track: 
Just like the get_artist function, this function does a search specifically for the track 
name. Although there are multiple results we take the first as it is most likely correct. 
We return the Track name, artist name, the artists id, and the Genre of the music.

get_genre:
This function does a specific genre search, and returns the top 10 tracks and the artists
of that genre. We do this because the returned tracks are genereally the artists most
popular songs and therefore the most likely to be enjoyed.

get_audio_features:
This function uses a track ID to get the specifics of the songs. The result breakdown is as follows:
Danceability: From 0 - 1, this is how "Danceable" the songs is. The closer to 1, the more danceable it is
Energy: Measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
Loudness: This is a scale that determines how loud the song is.
Speechiness: How much singing is within the song. The higher the number the more singing it has.
Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
Instrumentalness: Opposite of Speechiness, how much of the song is only instruments, the higher the number the more it has.
Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. 
Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
Tempo: The tempo is BPM (Beats Per Minute)
Time Signature: This is the time signature of the song that dictates how fast or slow the song is.
This function returns a few things, the original Data Frame, the list of the results (just the info from the results)
and the transpose of the Data Frame (this is so that it looks better when given options.)

get_plot_data: 
This function takes an artist ID list from the recommendation search and does a massive break down. 
First, it searches the first artist and grabs their most popular album. Then it iterates through the 
ablums songs and does a get_audio_features search to pull that songs data. It then saves that data into 
another dataframe and starts the loop again with the next artist. Because we are searching the artist,
then the album, then each track within the album, we have to limit the amount that we search to the top 3
artists. Because we are building a dataframe with every search it is very intensive.
We then return that dataframe to be altered by the plot function.