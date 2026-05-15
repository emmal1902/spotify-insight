from src.auth import get_spotify_client

def main():
    sp = get_spotify_client()

    user = sp.current_user()
    print("🎧 Connecté en tant que :", user["display_name"])
    print("ID :", user["id"])

if __name__ == "__main__":
    main()
