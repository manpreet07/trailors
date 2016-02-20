'''
Created on Jan 18, 2016

@author: singhm
'''


class Movie:
    """ This class stores movie information."""
    title = ""
    poster_image_url = ""
    trailer_youtube_url = ""

    def __init__(self, movietitle=None, moviebox=None, movielink=None):
        self.poster_image_url = moviebox
        self.title = movietitle
        self.trailer_youtube_url = movielink
