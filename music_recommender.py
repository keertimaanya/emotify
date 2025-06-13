import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


# Set up Spotify API client


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))


emotion_to_genre = {
    "joy": "pop",
    "sadness": "acoustic",
    "anger": "metal",
    "fear": "ambient",
    "love": "romance",
    "surprise": "edm",
    "neutral": "chill"
}

def get_genre_from_emotion(emotion):
    """Return genre mapped to the detected emotion"""
    return emotion_to_genre.get(emotion.lower(), "pop")  


# Fetch Spotify Tracks by Genre

def get_spotify_tracks_by_genre(genre, limit=5):
    """Search Spotify for songs in the given genre"""
    try:
        results = sp.search(q=f'genre:{genre}', type='track', limit=limit)
        tracks = []
        for item in results['tracks']['items']:
            tracks.append({
                "name": item['name'],
                "artist": item['artists'][0]['name'],
                "url": item['external_urls']['spotify']
            })
        return tracks
    except Exception as e:
        print("Error fetching tracks from Spotify:", e)
        return []
