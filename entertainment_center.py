import media
import fresh_tomatoes


dawn_of_the_dead = media.Movie(
    "Dawn Of The Dead",
    "https://upload.wikimedia.org/wikipedia/en/6/63/Dawn_of_the_dead.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Yd-z5wBeFTU")

# The Road movie: movie title, movie poster, and movie trailer
the_road = media.Movie(
    "The Road",
    "https://upload.wikimedia.org/wikipedia/en/a/a7/The_Road_movie_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=M8RuQrhVBvo")

# 28 Days Later movie: movie title, movie poster, and movie trailer
_28_days_later = media.Movie(
     "28 Days Later",
     "https://upload.wikimedia.org/wikipedia/en/e/e4/28_days_later.jpg",  # NOQA
     "https://www.youtube.com/watch?v=c7ynwAgQlDQ")

# Star Wars: movie title, movie poster, and movie trailer
star_wars = media.Movie(
    "Star Wars",
    "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1g3_CFmnU7k")

# The Witch: movie title, movie poster, and movie trailer
the_witch = media.Movie(
    "The Witch",
    "https://upload.wikimedia.org/wikipedia/en/b/bf/The_Witch_poster.png",  # NOQA
    "https://www.youtube.com/watch?v=iQXmlf3Sefg")

# Jaws: movie title, movie poster, and movie trailer
jaws = media.Movie(
    "Jaws",
    "https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=U1fu_sA7XhE")

# Alien: movie title, movie poster, and movie trailer
alien = media.Movie(
    "Alien",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LjLamj-b0I8")

movies = [dawn_of_the_dead, the_road, _28_days_later, star_wars, the_witch, jaws, alien]  # NOQA


fresh_tomatoes.open_movies_page(movies)
