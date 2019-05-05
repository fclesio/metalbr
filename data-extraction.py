from PyLyrics import *
import pandas as pd

# Brazilian Heavy Metal Bands
artistas = ['sepultura', 'angra']

lyrics_df = []

for artist in artistas:
    # Get all albuns
    albums = PyLyrics.getAlbums(singer=artist)

    for album in albums:
        tracks = album.tracks()

        for track in tracks:
            lyrics = track.getLyrics()
            music_name = track.name
            lyrics_df.append((artist, album, music_name, lyrics))
            print(f'Artist: {artist}, Album: {album}, Music Name: {music_name}')


# Build DF
df_lyrics = pd.DataFrame(lyrics_df)

# Dump to CSV
df_lyrics.to_csv('rebirth-remains.csv')
