import fresh_tomatoes  # importing file fresh_tomatoes.py
import parents  # importing file parents.py

# making an instance of Movie class
toystory = parents.Movie(
    "Toy Story",
    "Andy's favourite toy, Woody, is worried that after Andy receives his"
    " birthday gift, a new toy called Buzz Lightyear, his importance may "
    "get reduced.",
    "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx"
    "_5670999f.jpeg?region=0%2C0%2C300%2C450",
    "https://www.youtube.com/watch?v=SgoiKLFBA3Q")

# making an instance of Movie class
inferno = parents.Movie(
    "Inferno",
    "After waking up with amnesia in a hospital, Robert Langdon teams up with"
    " Sienna Brooks, one of his doctors, to protect the world from the evil"
    " plan of a mad scientist.",
    "http://www.sonypictures.com/movies/inferno/assets/images/onesheet.jpg",
    "https://www.youtube.com/watch?v=RH2BD49sEZI")

# making an instance of Movie class
school_of_rock = parents.Movie(
    "School Of Rock",
    "Dewey Finn, an amateur rock enthusiast, slyly takes up his friend's "
    "substitute teacher's job. Bearing no qualifications for it, he instead"
    " starts training the students to be a band.",
    "https://images-na.ssl-images-amazon.com/images/I/51XB8K6WPEL._SY445_.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

# making an instance of Movie class
hungergames = parents.Movie(
    "Hunger Games",
    "The Hunger Games film series consists of four science fiction dystopian"
    " adventure films based on The Hunger Games trilogy of novels, by the "
    "American author Suzanne Collins.",
    "https://images-na.ssl-images-amazon.com/images/I/41LPBRNaVCL._SX355_BO1"
    ",204,203,200_.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")

# making an instance of Movie class
angels_and_demons = parents.Movie(
    "Angels and Demons",
    "A symbologist tries his best to stop a secret society from destroying"
    " Vatican City. He tries to decipher various clues in the process, most"
    " of which lead him to the four altars of science.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Angels_and_demons"
    ".jpg/220px-Angels_and_demons.jpg",
    "https://www.youtube.com/watch?v=dhMQVeL8Kqw")

# making an instance of Movie class
titanic = parents.Movie(
    "Titanic",
    "Seventeen-year-old Rose hails from an aristocratic family and is set to"
    " be married. When she boards the Titanic, she meets Jack Dawson, an "
    "artist, and falls in love with him.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY"
    "2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._"
    "V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

# making an instance of Movie class
red_sparrow = parents.Movie(
    "Red Sparrow",
    "Prima ballerina Dominika Egorova faces a bleak and uncertain future after"
    " she suffers an injury that ends her career. She soon turns to Sparrow"
    " School, a secret intelligence service that trains exceptional young"
    " people to use their minds and bodies as weapons.",
    "https://assets.voxcinemas.com/posters/P_HO00005162.jpg",
    "https://www.youtube.com/watch?v=PmUL6wMpMWw")

# making an instance of Movie class
death_wish = parents.Movie(
    "Death Wish",
    "Dr. Paul Kersey is a surgeon who often sees the consequences of the"
    " city's violence in the emergency room. When home intruders brutally"
    " attack his wife and young daughter, Kersey becomes obsessed with "
    "delivering vigilante justice to the perpetrators.",
    "https://www.dvdsreleasedates.com/posters/800/D/Death-Wish-2017-"
    "movie-poster.jpg",
    "https://www.youtube.com/watch?v=HzILu6yyA20")

# making a list of all the movies
movies_list = [toystory, inferno, school_of_rock, hungergames,
               angels_and_demons, titanic, red_sparrow, death_wish]
"""passing the list as a parameter to the 'open_movies_page' method inside
'fresh_tomatoes.py'"""
fresh_tomatoes.open_movies_page(movies_list)
