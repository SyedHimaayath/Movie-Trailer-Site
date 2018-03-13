class Movie():
    """init function takes in all the neccessary arguments starting with self,
representing the particular movie selected"""
    def __init__(self, title, storyline, movie_poster, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_youtube_url
