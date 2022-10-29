import numpy as np
import pandas as pd

def getDanceSongsRecommendations(emotion):
    df_danceability= df_new[df_new['danceability']>=0.5].sort_values('danceability', ascending=False)
    df_top_10 = df_danceability.iloc[:11]
    topDanceSongs = df_top_10["track_name"].tolist()
    return topDanceSongs

def getSadSongsRecommendations(emotion):
    df_sad= df_new[df_new['sadness']>=0.5].sort_values('sadness', ascending=False)
    df_top_10 = df_sad.iloc[:11]
    topSadSongs = df_top_10["track_name"].tolist()
    return topSadSongs

def SongRecommender(emotion):
    if emotion=="happy":
        print(getDanceSongsRecommendations(emotion))
    else:
        print(getSadSongsRecommendations(emotion))

df = pd.read_csv("allmusics.csv")

df_new = df[['track_name','night/time','family/gospel','danceability','sadness']].copy()

SongRecommender("sad")





