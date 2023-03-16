"""
Gra w "wisielca". Jeden z użytkowników wprowadza słowo, które drugi z użytkowników ma odgadnąć.
Program wyrysowuje tyle "_" ile liter ma podane słowo.
Odgadujący podaje literka po literce. Jeżeli litera występuje - należy zamienić "_" na literę (lub litery, jeżeli jest ich więcej).
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


class Hangman:
    def __init__(self, word):
        self.word = word

    def print_fields(self):
        fields = "_"
        counter = 0
        for n in self.word:
            # print("_", end="\t")
            counter += 1
        return fields * counter

    def count_fields(self):
        return len(self.word)


# Deklaracja słowa
print("Wprowadź słowo:")
word_input = input()

game1 = Hangman(word_input)
word_length = game1.count_fields()
print(f"Pola słowa to: {game1.print_fields()}")
print(f"słowo sklada się z {word_length} liter")

number_of_attemps = 11
print(f"Masz {number_of_attemps} prób")

used_letters = []
counter = 0
word_result = ""
while number_of_attemps > 0:
    print(f"Użyte do tej pory litery: {used_letters}")
    print("Podaj literę")
    letter = input()
    if word_input.__contains__(letter):
        print(f"litera {letter} występuje w słowie")
        word_result = word_input.replace("_", letter, counter)
    else:
        print(f"litera {letter} nie występuje w słowie")
        number_of_attemps -= 1
        used_letters.append(letter)
        print(f"Pozostało {number_of_attemps} prób")
    counter += 1
    print(word_result)
