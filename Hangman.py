"""
Gra w "wisielca". Jeden z użytkowników wprowadza słowo, które drugi z użytkowników ma odgadnąć.
Program wyrysowuje tyle "_" ile liter ma podane słowo.
Odgadujący podaje literka po literce. Jeżeli litera występuje - należy zamienić "_" na literę (lub litery,
jeżeli jest ich więcej).
Jeżeli litera nie występuje to należy zacząć rysowanie szubienicy i wisielca.
Kolejność rysowania szubienicy:
1. Podstawa
2. Pionowy maszt wystający ze środka podstawy
3. Pozioma belka, do której przywiązany będzie sznur
4. Ukosna belka (wspornik) podtrzymująca belkę poziomą
5. Sznur
Kolejność rysowania wisielca:
1. Głowa
2. Tułów
3. Ręka
5. Druga ręka
6. Noga
7. Druga noga
"""

import os


class Hangman:
    def __init__(self):
        self.correct_guess = []
        self.secret_word = ""
        self.remaining_attempts = 7
        self.incorrect_guess = []

    def get_word(self):
        self.secret_word = input("Wprowadź słowo do odgadnięcia: ")

    def clear_console(self):
        print("\n"*10)

    def guess_letter(self):
        tmp_word = ""
        guess = input("Wprowadź literę: ")
        if guess in self.secret_word:
            self.correct_guess.append(guess)
        for letter in self.secret_word:
            if letter in self.correct_guess:
                tmp_word += letter
            else:
                tmp_word += "_"
        print("aktualny status: ", tmp_word)
        if tmp_word == self.secret_word:
            print("Słowo zostało odgadnięte! Gratulacje!")
        else:
            if guess not in self.secret_word:
                print(f"Litera {guess} nie występuje w słowie")
                self.incorrect_guess.append(guess)
                print("typowane litery: ", sorted(self.incorrect_guess))
                self.remaining_attempts -= 1
        # print(f"pozostało {self.remaining_attempts} prób")

    def drawing_hangman(self):
        if self.remaining_attempts == 7:
            print("    ______")
            print("    |    |")
            print("         |")
            print("         |")
            print("         |")
            print("         |")
            print("         |")
            print("^^^^^^^^^^")
        if self.remaining_attempts == 6:
            print("    ______")
            print("    |    |")
            print("    O    |")
            print("         |")
            print("         |")
            print("         |")
            print("         |")
            print("^^^^^^^^^^")
        if self.remaining_attempts == 5:
            print("    ______")
            print("    |    |")
            print("    O    |")
            print("    |    |")
            print("         |")
            print("         |")
            print("         |")
            print("^^^^^^^^^^")
        if self.remaining_attempts == 4:
            print("    ______")
            print("    |    |")
            print("    O    |")
            print("    |\   |")
            print("         |")
            print("         |")
            print("         |")
            print("^^^^^^^^^^")
        if self.remaining_attempts == 3:
            print("    ______")
            print("    |    |")
            print("    O    |")
            print("   /|\   |")
            print("         |")
            print("         |")
            print("         |")
            print("^^^^^^^^^^")
        if self.remaining_attempts == 2:
            print("    ______")
            print("    |    |")
            print("    O    |")
            print("   /|\   |")
            print("    |    |")
            print("         |")
            print("         |")
            print("^^^^^^^^^^")
        if self.remaining_attempts == 1:
            print("    ______")
            print("    |    |")
            print("    O    |")
            print("   /|\   |")
            print("    |    |")
            print("     \   |")
            print("         |")
            print("^^^^^^^^^^")

    def play(self):
        while self.remaining_attempts > 0:
            self.drawing_hangman()
            self.guess_letter()
        else:
            print("Przegrana!".upper())
            print("    ______")
            print("    |    |")
            print("    O    |")
            print("   /|\   |")
            print("    |    |")
            print("   / \   |")
            print("         |")
            print("^^^^^^^^^^")


game = Hangman()
game.get_word()
game.clear_console()
game.play()
