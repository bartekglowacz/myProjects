class RockPaperScissors:
    # reszta kodu jest taka sama jak w Twoim przykładzie

    def Play(self):
        list_of_choices = [[self.list_of_players[player], self.SetSign()] for player in
                           range(0, len(self.list_of_players))]
        print(list_of_choices)

        # utworzenie listy zawierającej tylko wybory graczy
        player_choices = [choice[1] for choice in list_of_choices]

        # decydowanie o zwycięzcy
        if "rock" in player_choices and "paper" in player_choices and "scissors" in player_choices:
            print("Remis")
        elif "rock" in player_choices and "paper" in player_choices:
            print("Papier owija kamień!")
        elif "rock" in player_choices and "scissors" in player_choices:
            print("Kamień tępi nożyce!")
        elif "paper" in player_choices and "scissors" in player_choices:
            print("Nożyce tną papier!")
        else:
            print("Nieznany wynik gry")

        for x in range(0, len(list_of_choices)):
            player_name = list_of_choices[x][0]
            player_choice = list_of_choices[x][1]
            print(f"Gracz {player_name} wybrał {player_choice}")
