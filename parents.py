class Movie():
    """
    Class Movie is the parent class containing all the details

    contains an '__init__' method
    """
    def __init__(self, title, storyline, movie_poster, trailer_youtube_url):
        """
        init function is the initializing function of class Movie

        Parameters
        ----------
        self :
            reference to the current instance of the class
        title : str
            takes in the title of the movie
        storyline : str
            takes in the stoyline o fthe movie
        movie_poster: str
            url that points to the poster of a particular movie
        trailer_youtube-url : str
            url to the movie's trailer
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_youtube_url
