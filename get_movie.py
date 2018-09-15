#!/usr/bin/env python
'''
Module to initialise class Movie.

This module has a class Movie which has a constructor, that
construct the object and respective properties.
'''


# C0301 - To disable 'line too long' message
# pylint: disable-msg=C0301
# C1001 - To diable 'Old-style class defined' message
# pylint: disable-msg=C1001
# R0903 - To diable 'Too few Public Methods' message
# pylint: disable-msg=R0903
# E0213 - To diable 'Method should have 'self' as first argument' message
# pylint: disable-msg=E0213
# R0913 - To disable 'Too many method arguments' message
# pylint: disable-msg=R0913
class Movie:
    '''
    The Class Movie will get the title, image link, trailer link, etc.
    and pass it to create html page.

    The class expects 6 arguments to be passed when creating it's instance.
    All arguments are expected to be string.
    '''
    # Iniate Constructor for the class
    def __init__(obj, title, short, genre, rating, movie_image, movie_trailer):
        '''
        Constructor method for class Movie.

        The constructor will initiate the object and the
        object properties respectievely.

        Parameters:
        -----------

        tile: string
            The argument will initialise the title of the movie.

        short: string
            The argument will initialise the story line of the movie.

        genre: string
            The argument will initialise the genre of the movie.

        rating: string
            The argument will initialise the rating for the movie.

        rating: string
            The argument will initialise the movie poster URL.

        rating: string
            The argument will initialise the youtube trailer URL.

        '''
        # Assign param values to object properties
        obj.title = title
        obj.short = short
        obj.genre = genre
        obj.rating = rating
        obj.movie_image = movie_image
        obj.movie_trailer = movie_trailer
