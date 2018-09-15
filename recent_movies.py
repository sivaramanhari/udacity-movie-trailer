#!/usr/bin/env python
'''
The script that append different movies and call create_browser module that creates html file.
'''

# C0301 - To disable 'line too long' message
# pylint: disable-msg=C0301

import create_browser
import get_movie

# To add new movie, Copy one of the movie method and edit it with respective values.
def nun_movie():
    '''
    Defines and constructs variables for movie nun
    '''
    title = "The Nun"
    short = "When a young nun at a cloistered abbey in Romania takes her own life, a priest with a haunted past and a novitiate on the threshold."
    genre = "Horror"
    rating = "6/10"
    movie_image = "https://upload.wikimedia.org/wikipedia/en/3/34/TheNunPoster.jpg"
    movie_trailer = "https://www.youtube.com/watch?v=pzD9zGcUNrw"
    # Calling Class Movie
    movie = get_movie.Movie(title, short, genre, rating, movie_image, movie_trailer)
    return movie

def mi_movie():
    '''
    Defines and constructs variables for movie nun
    '''
    title = "Mission: Impossible - Fallout"
    short = "Ethan Hunt and the IMF team join forces with CIA assassin August Walker to prevent a disaster of epic proportions."
    genre = "Action"
    rating = "8.1/10"
    movie_image = "https://m.media-amazon.com/images/M/MV5BMTk3NDY5MTU0NV5BMl5BanBnXkFtZTgwNDI3MDE1NTM@._V1_.jpg"
    movie_trailer = "https://www.youtube.com/watch?v=wb49-oV0F78"
    # Calling Class Movie
    movie = get_movie.Movie(title, short, genre, rating, movie_image, movie_trailer)
    return movie

def jurassic_movie():
    '''
    Defines and constructs variables for movie nun
    '''
    title = "Jurassic World: Fallen Kingdom"
    short = "Three years after the destruction of the Jurassic World theme park, Owen Grady and Claire Dearing return to the island of Isla Nublar to save the remaining dinosaurs from a volcano that's about to erupt."
    genre = "Action"
    rating = "6.4/10"
    movie_image = "https://vignette.wikia.nocookie.net/cinemorgue/images/d/df/322699f120c17c2728457969b59af12c.jpg/revision/latest?cb=20180325190743"
    movie_trailer = "https://www.youtube.com/watch?v=vn9mMeWcgoM"
    # Calling Class Movie
    movie = get_movie.Movie(title, short, genre, rating, movie_image, movie_trailer)
    return movie

def christopher_movie():
    '''
    Defines and constructs variables for movie nun
    '''
    title = "Christopher Robin"
    short = "Christopher Robin -- now a family man living in London -- receives a surprise visit from his old childhood pal, Winnie-the-Pooh."
    genre = "Comedy"
    rating = "7.7/10"
    movie_image = "https://upload.wikimedia.org/wikipedia/en/a/a9/Christopher_Robin_poster.png"
    movie_trailer = "https://www.youtube.com/watch?v=0URpDxIjZrQ"
    # Calling Class Movie
    movie = get_movie.Movie(title, short, genre, rating, movie_image, movie_trailer)
    return movie

def transylvania_movie():
    '''
    Defines and constructs variables for movie nun
    '''
    title = "Hotel Transylvania 3: Summer Vacation"
    short = "Mavis surprises Dracula with a family voyage on a luxury Monster Cruise Ship so he can take a vacation from providing everyone else's vacation at the hotel."
    genre = "Animation/Comedy"
    rating = "6.3/10"
    movie_image = "https://www.dvdsreleasedates.com/posters/800/H/Hotel-Transylvania-3-A-Monster-Vacation-2018-movie-poster.jpg"
    movie_trailer = "https://www.youtube.com/watch?v=Ku52zNnft8k"
    # Calling Class Movie
    movie = get_movie.Movie(title, short, genre, rating, movie_image, movie_trailer)
    return movie

def incredibles_movie():
    '''
    Defines and constructs variables for movie nun
    '''
    title = "Incredibles 2"
    short = "Everyone's favorite family of superheroes is back in 'Incredibles 2' but this time Helen is in the spotlight, leaving Bob at home with Violet and Dash to navigate the day-to-day heroics of 'normal' life."
    genre = "Animation/Action"
    rating = "8.1/10"
    movie_image = "https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg"
    movie_trailer = "https://www.youtube.com/watch?v=i5qOzqD9Rms"
    # Calling Class Movie
    movie = get_movie.Movie(title, short, genre, rating, movie_image, movie_trailer)
    return movie

def append_movies():
    '''
    Call all movie methods, define movie list used as the parameters for the method open_movies_page that creates the HTML page
    '''
    # Once created method add the method call here
    nun = nun_movie()
    mim = mi_movie()
    jurassic = jurassic_movie()
    christopher = christopher_movie()
    transylvania = transylvania_movie()
    incredibles = incredibles_movie()

    # After calling the method, add the variable assigned to the respective method to the below moves list.
    movies = [nun, mim, jurassic, christopher, transylvania, incredibles]
    # Calls the method that create HTML page
    create_browser.open_movies_page(movies)

append_movies()
