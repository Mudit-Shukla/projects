from pprint import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


year = input("Which year you want to go, Enter in YYYY-MM-DD format")
URL =  "https://www.billboard.com/charts/hot-100"

CLIENT_SECRET = "98d14c5c7eb14853bb27f04204ea0753"
CLIENT_ID = "8ebd53a2a5504dd590f0d9a605a645cc"
username = "day_dreamer"

spotifyObject = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        redirect_uri = "http://example.com",
        client_id= CLIENT_ID,
        client_secret= CLIENT_SECRET,
        scope = "playlist-modify-public",
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = spotifyObject.current_user()["id"]
print(user_id)

playlist_name = input("Enter playlist name: ")
playlist_description = input("Enter playlist description: ")

spotifyObject.user_playlist_create(user= user_id, name=playlist_name, description=playlist_description, public=True)


response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
songs_list = soup.find_all(name = "span", class_ = "chart-element__information__song text--truncate color--primary")
songs_uri_list = []

for song in songs_list:
    res = spotifyObject.search(q= song)
    # sond_id = (res["tracks"]["items"][0]["artists"][0]["id"])
    song_uri = (res["tracks"]["items"][0]["uri"])
    songs_uri_list.append(song_uri)
    # print(len(songs_uri_list))


list_of_playlist = spotifyObject.user_playlists(user = user_id)
print((list_of_playlist))

required_playlist = (list_of_playlist["items"][0]["id"])

(spotifyObject.user_playlist_add_tracks(user=user_id, playlist_id=required_playlist,tracks=songs_uri_list))
