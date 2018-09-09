#!/usr/bin/env python

import create_browser
import getMovie

def nun_movie():
  title = "The Nun"
  short = "When a young nun at a cloistered abbey in Romania takes her own life, a priest with a haunted past and a novitiate on the threshold."
  genre = "Horror"
  rating = "6/10"
  movie_image = "https://upload.wikimedia.org/wikipedia/en/3/34/TheNunPoster.jpg"
  movie_trailer = "https://www.youtube.com/watch?v=pzD9zGcUNrw"
  movie = getMovie.Movie(title, short, genre, rating, movie_image, movie_trailer)
  return movie

def mi_movie():
  title = "Mission: Impossible - Fallout"
  short = "Ethan Hunt and the IMF team join forces with CIA assassin August Walker to prevent a disaster of epic proportions."
  genre = "Action"
  rating = "8.1/10"
  movie_image = "https://m.media-amazon.com/images/M/MV5BMTk3NDY5MTU0NV5BMl5BanBnXkFtZTgwNDI3MDE1NTM@._V1_.jpg"
  movie_trailer = "https://www.youtube.com/watch?v=wb49-oV0F78"
  movie = getMovie.Movie(title, short, genre, rating, movie_image, movie_trailer)
  return movie

def jurassic_movie():
  title = "Jurassic World: Fallen Kingdom"
  short = "Three years after the destruction of the Jurassic World theme park, Owen Grady and Claire Dearing return to the island of Isla Nublar to save the remaining dinosaurs from a volcano that's about to erupt."
  genre = "Action"
  rating = "6.4/10"
  movie_image = "https://vignette.wikia.nocookie.net/cinemorgue/images/d/df/322699f120c17c2728457969b59af12c.jpg/revision/latest?cb=20180325190743"
  movie_trailer = "https://www.youtube.com/watch?v=vn9mMeWcgoM"
  movie = getMovie.Movie(title, short, genre, rating, movie_image, movie_trailer)
  return movie

def christopher_movie():
  title = "Christopher Robin"
  short = "Christopher Robin -- now a family man living in London -- receives a surprise visit from his old childhood pal, Winnie-the-Pooh."
  genre = "Comedy"
  rating = "7.7/10"
  movie_image = "https://upload.wikimedia.org/wikipedia/en/a/a9/Christopher_Robin_poster.png"
  movie_trailer = "https://www.youtube.com/watch?v=0URpDxIjZrQ"
  movie = getMovie.Movie(title, short, genre, rating, movie_image, movie_trailer)
  return movie

def transylvania_movie():
  title = "Hotel Transylvania 3: Summer Vacation"
  short = "Mavis surprises Dracula with a family voyage on a luxury Monster Cruise Ship so he can take a vacation from providing everyone else's vacation at the hotel."
  genre = "Animation/Comedy"
  rating = "6.3/10"
  movie_image = "https://www.dvdsreleasedates.com/posters/800/H/Hotel-Transylvania-3-A-Monster-Vacation-2018-movie-poster.jpg"
  movie_trailer = "https://www.youtube.com/watch?v=Ku52zNnft8k"
  movie = getMovie.Movie(title, short, genre, rating, movie_image, movie_trailer)
  return movie

def incredibles_movie():
  title = "Incredibles 2"
  short = "Everyone's favorite family of superheroes is back in 'Incredibles 2' but this time Helen is in the spotlight, leaving Bob at home with Violet and Dash to navigate the day-to-day heroics of 'normal' life."
  genre = "Animation/Action"
  rating = "8.1/10"
  movie_image = "https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg"
  movie_trailer = "https://www.youtube.com/watch?v=i5qOzqD9Rms"
  movie = getMovie.Movie(title, short, genre, rating, movie_image, movie_trailer)
  return movie

def append_movies():
  nun = nun_movie()
  mi = mi_movie()
  jurassic = jurassic_movie()
  christopher = christopher_movie()
  transylvania = transylvania_movie()
  incredibles = incredibles_movie()

  movies = [nun, mi, jurassic, christopher, transylvania, incredibles]
  create_browser.open_movies_page(movies)

append_movies()

