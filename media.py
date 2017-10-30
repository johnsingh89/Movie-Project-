import webbrowser


class Video():
    # This class provies a way to store movie related information """
    def __init__(self, movie_title, poster_image):
        self.title = movie_title
        self.poster_image_url = poster_image


class Movie(Video):
    # Movie class is calling the parent class for the movie title and poster image # NOQA
    def __init__(self, movie_title, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, poster_image)
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Allows the web browser to open and play a video
        webbrowser.open(self.trailer_youtube_url)
