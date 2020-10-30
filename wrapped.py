#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:08:46 2020

@author: Ayca
"""

import json
import pandas as pd
with open('StreamingHistory0.json') as json_file:
    data = json.load(json_file)
with open('StreamingHistory1.json') as json_file:
    data1 = json.load(json_file)
data+=data1
df = pd.DataFrame(data)
df = df[df.msPlayed != 0]
df = df.groupby(['artistName','trackName'], as_index=False)['msPlayed'].sum()

df['seconds']=(df.msPlayed/1000)
df['minutes']=df['seconds']/60
df['hours']=df['minutes']/60

# print(df.columns)

df_time = df.sort_values(by=['msPlayed'],ascending=False)
df_time = df_time.reset_index(drop=True)
# print(df.head)
# print(df_time.head)


print("\nTotal time spent in Spotify(in minutes): {:.2f}, (in hours): {:.2f}".format(df['minutes'].sum(),df['minutes'].sum()/60))
top_artists = df.groupby(['artistName'], as_index=False)['msPlayed'].sum()
top_artists = top_artists.sort_values(by=['msPlayed'],ascending=False)
top_artists = top_artists.reset_index(drop=True)
#print(top_artists['artistName'].head)

print("\nYou listened these artists this year at most: \n", top_artists[:5]['artistName'])

df_track = df.groupby(['artistName','trackName'], as_index=False)['msPlayed'].sum()
df_track = df_track.sort_values(by=['msPlayed'],ascending=False)
df_track = df_track.reset_index(drop=True)
print("\nTop tracks of the year!\n",df_track[:5])
print("\nMost listened track of year!:\n {} by {}, {:.2f} minutes, {:.2f} hours in total".format(df_time.iloc[0]['trackName'],
                                                                                      df_time.iloc[0]['artistName'],
                                                                                      df_time.iloc[0]['minutes'],
                                                                                      df_time.iloc[0]['minutes'].sum()/60))