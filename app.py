from src.auth import get_spotify_client
from src.data_fetch import get_top_tracks
from src.analysis import tracks_to_df

def main():
    sp = get_spotify_client()

    tracks = get_top_tracks(sp)
    df = tracks_to_df(tracks)

    print(df.head())

if __name__ == "__main__":
    main()
