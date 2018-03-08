class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    def __init__(self, title, duration, movie_storyline, movie_poster, movie_youtube_url):
        Video.__init__(title, duration)
        self.storyline = movie_storyline
        self.poster = movie_poster
        self.youtube_url = movie_youtube_url

