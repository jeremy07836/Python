class Song:
    """Class to represent a song
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds
    """

    def __init__(self, title, artist, duration=0):
        """Song init method
        Args:
            title (str): Initialises the `title` attribute
            artist (Artist): An Artist object representing the songs creator
            duration (Optional[int]): Initial value of the `duration` attribute
                will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration
