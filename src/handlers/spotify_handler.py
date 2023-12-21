from typing import Any

from spotipy import SpotifyClientCredentials, Spotify, SpotifyOAuth

from src.handlers.timed_handler import TimedHandler


class SpotifyHandler(TimedHandler):
    auth_manager: SpotifyOAuth = None
    spotify: Spotify = None

    currently_playing: Any = None
    is_playing = False

    @property
    def seconds_pause(self) -> int:
        return 10

    def handle(self, ctx):
        if super().handle(ctx):
            if not self.auth_manager or not self.spotify:
                self.auth_manager = SpotifyOAuth(
                    redirect_uri=ctx.get_config("spotify_redirect_uri"),
                    client_id=ctx.get_config("spotify_client_id"),
                    client_secret=ctx.get_config("spotify_client_secret"),
                    scope=ctx.get_config("spotify_user_scope")
                )
                self.spotify = Spotify(auth_manager=self.auth_manager)

            current_song = self.spotify.currently_playing()

            if current_song is not None:
                self.is_playing = current_song["is_playing"]
                self.currently_playing = current_song["item"]
            else:
                self.is_playing = False
                self.currently_playing = self.spotify.current_user_recently_played(limit=1)["items"][0]["track"]

    def get_artist(self) -> str:
        return self.currently_playing["artists"][0]["name"]

    def get_track_name(self) -> str:
        title = self.currently_playing["name"]

        return (title[:25] + '..') if len(title) > 25 else title