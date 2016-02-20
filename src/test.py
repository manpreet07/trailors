'''
Created on Jan 18, 2016

@author: singhm
'''

from movie import Movie
from fresh_tomatoes import open_movies_page

""" This module runs the application."""

# Movie 1
movieTitle = "Terminator Salvation"
youtubeUrl = "https://www.youtube.com/watch?v=6GmLfivKQL8"
boxImage = "..\src\images\TerminatorSalvation.jpg"
terminator_salvation = Movie(movieTitle, boxImage, youtubeUrl)

# Movie 2
movieTitle2 = "Jurrasic World"
youtubeUrl2 = "https://www.youtube.com/watch?v=RFinNxS5KN4"
boxImage2 = "..\src\images\JurrasicWorld.jpg"
jurrasic_world = Movie(movieTitle2, boxImage2, youtubeUrl2)

# Movie 3
movieTitle3 = "Interstellar"
youtubeUrl3 = "https://www.youtube.com/watch?v=Lm8p5rlrSkY"
boxImage3 = "..\src\images\Interstaller.jpg"
interstellar = Movie(movieTitle3, boxImage3, youtubeUrl3)

movies = [terminator_salvation, jurrasic_world, interstellar]
open_movies_page(movies)
