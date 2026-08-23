class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def categorize(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Rating:", self.rating)
        print("Ticket Price: ₹", self.ticket_price)
        print("Category:", self.categorize())
        print("-" * 30)


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\nMovie Details")
        print("=" * 40)

        for movie in self.movies:
            movie.display()


# Main Program
cinema = Cinema()

m1 = Movie("3 Idiots", 9.0, 250)
m2 = Movie("Chhichhore", 7.5, 200)
m3 = Movie("Example Movie", 4.0, 150)

cinema.add_movie(m1)
cinema.add_movie(m2)
cinema.add_movie(m3)

cinema.display_movies()