def get_top_tracks(sp):
    return sp.current_user_top_tracks(limit=20)

def get_top_artists(sp):
    return sp.current_user_top_artists(limit=20)
