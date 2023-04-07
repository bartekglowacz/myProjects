import random


class RockPaperScissors:
    def __init__(self):
        self.list_of_players = None

    def Players(self):
        number_of_players = 2
        self.list_of_players = ["Player" + str(i) for i in range(1, number_of_players + 1)]
        return self.list_of_players

    def SetSign(self):
        choice = random.randint(1, 3)
        if choice == 1:
            sign = "kamień"
        if choice == 2:
            sign = "papier"
        if choice == 3:
            sign = "nożyce"
        return sign

    def Play(self):
        list_of_choices = [[self.list_of_players[player], self.SetSign()] for player in
                           range(0, len(self.list_of_players))]
        print(list_of_choices)
        for x in range(0, len(list_of_choices)):
            player_name = list_of_choices[x][0]
            player_choice = list_of_choices[x][1]
            # result_list.append(player_choice)
            print(f"Gracz {player_name} wybrał {player_choice}")
        result_list = [choice[1] for choice in list_of_choices]
        if "kamień" in result_list and "papier" in result_list:
            print("Papier owija kamień!")
        elif "kamień" in result_list and "nożyce" in result_list:
            print("Kamień tępi nożyce!")
        elif "papier" in result_list and "nożyce" in result_list:
            print("Nożyce tną papier!")
        else:
            print("Remis!")


game = RockPaperScissors()
game.Players()
game.Play()
