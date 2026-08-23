class Player:
    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs

    def categorize(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name:", self.player_name)
        print("Jersey Number:", self.jersey_number)
        print("Runs:", self.runs)
        print("Category:", self.categorize())
        print("-" * 35)


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        print("\nCricket Team Player Details")
        print("=" * 40)

        for player in self.players:
            player.display()


# Main Program
team = Team()

p1 = Player("Virat", 18, 1200)
p2 = Player("Rohit", 45, 750)
p3 = Player("Rahul", 1, 350)

team.add_player(p1)
team.add_player(p2)
team.add_player(p3)

team.display_players()