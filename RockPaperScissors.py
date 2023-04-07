import random


class RockPaperScissors:
    def __init__(self):
        self.list_of_players = None

    def Players(self):
        print("Ilu graczy bierze udział w grze?")
        number_of_players = int(input())
        self.list_of_players = ["Player" + str(i) for i in range(1, number_of_players + 1)]
        return self.list_of_players

    def SetSign(self):
        choice = random.randint(1, 3)
        if choice == 1:
            sign = "rock"
        if choice == 2:
            sign = "paper"
        if choice == 3:
            sign = "scissors"
        return sign

    def Play(self):
        for player in range(0, len(self.list_of_players)):
            print(f"Gracz {self.list_of_players[player]} wybrał {self.SetSign()}")


game = RockPaperScissors()
game.Players()
game.Play()
