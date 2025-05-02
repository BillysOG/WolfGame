
class Game:
    games_played = 0
    def __init__(self,name,hours_played,size):
        self.name = name
        self.hours_played = hours_played
        self.size = size
        Game.games_played += 1
        
    def __str__(self):
        return f"The title of the game is '{self.name}'"
    
    def __eq__(self,other):
        return self.name == other.name
    
    def __lt__(self, other):
        if self.hours_played < other.hours_played and self.size < other.size:
            print(f"'{self.name}' has less playtime and is smaller than '{other.name}'")
            return True
        elif self.hours_played < other.hours_played:
            print(f"'{self.name}' has less playtime than '{other.name}'")
            return True
        elif self.size < other.size:
            print(f"'{self.name}' is smaller than '{other.name}'")
            return True
        return False
    
    def __gt__(self, other):
        if self.hours_played > other.hours_played and self.size > other.size:
            print(f"'{self.name}' has more playtime and is bigger than '{other.name}'")
            return True
        elif self.hours_played > other.hours_played:
            print(f"'{self.name}' has more playtime than '{other.name}'")
            return True
        elif self.size > other.size:
            print(f"'{self.name}' is bigger than '{other.name}'")
            return True
        return False
    
game1 = Game("Hollow Knight", 80, 5)
game2 = Game("Ultrakill", 90, 2)
game3 = Game("Genshin Impact", 500, 75)

print(game1 > game3)
print(game3 > game2)
        