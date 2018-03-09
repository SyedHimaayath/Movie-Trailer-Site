import fresh_tomatoes
import parents

toystory = parents.Movie("Toy Story","Bla bla bla","https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450","https://www.youtube.com/watch?v=SgoiKLFBA3Q")

inferno = parents.Movie("Inferno","Bla bla bla","http://www.sonypictures.com/movies/inferno/assets/images/onesheet.jpg","https://www.youtube.com/watch?v=RH2BD49sEZI")

school_of_rock = parents.Movie("School Of Rock","Bla bla bla","https://images-na.ssl-images-amazon.com/images/I/51XB8K6WPEL._SY445_.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

hungergames = parents.Movie("Hunger Games","Bla bla bla","https://images-na.ssl-images-amazon.com/images/I/41LPBRNaVCL._SX355_BO1,204,203,200_.jpg","https://www.youtube.com/watch?v=mfmrPu43DF8")

angels_and_demons = parents.Movie("Angels and Demons","Bla bla bla","https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Angels_and_demons.jpg/220px-Angels_and_demons.jpg","https://www.youtube.com/watch?v=dhMQVeL8Kqw")

titanic = parents.Movie("Titanic","Bla bla bla","https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

red_sparrow = parents.Movie("Red Sparrow","Bla bla bla","https://assets.voxcinemas.com/posters/P_HO00005162.jpg","https://www.youtube.com/watch?v=PmUL6wMpMWw")

death_wish = parents.Movie("Death Wish","Bla bla bla","https://www.dvdsreleasedates.com/posters/800/D/Death-Wish-2017-movie-poster.jpg","https://www.youtube.com/watch?v=HzILu6yyA20")

movies_list = [toystory, inferno, school_of_rock, hungergames, angels_and_demons, titanic, red_sparrow, death_wish]

fresh_tomatoes.open_movies_page(movies_list)
