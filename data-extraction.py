from PyLyrics import *
import pandas as pd

# Brazilian Heavy Metal Bands
artistas = ['sepultura', 'angra']

lyrics_df = []

# Get all music from all albuns
for artista in artistas:
    albums = PyLyrics.getAlbums(singer=artista)

    for i in range(len(albums)):
        myalbum = albums[i]
        tracks = myalbum.tracks()

        for track in tracks:
            lyrics = track.getLyrics()
            lyrics_df.append((artista, myalbum, lyrics))

# Build DF
df_lyrics = pd.DataFrame(lyrics_df)

# Check shape and format
print(df_lyrics.shape)
print(df_lyrics.head(5))

# Dump to CSV
df_lyrics.to_csv('rebirth-remains.csv')
