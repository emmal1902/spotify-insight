import pandas as pd

def tracks_to_df(tracks):
    data = []

    for item in tracks["items"]:
        data.append({
            "track": item["name"],
            "artist": item["artists"][0]["name"]
        })

    return pd.DataFrame(data)
