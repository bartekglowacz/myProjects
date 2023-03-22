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


class Hangman:
    def __init__(self, word):
        self.word = word

    # rysuje tyle "_" ile jest liter w słowie
    def print_fields(self):
        fields = "_"
        field_counter = 0
        for _ in self.word:
            # print("_", end="\t")
            field_counter += 1
        return fields * field_counter

    # liczy ile pól jest w słowie
    def count_fields(self):
        return len(self.word)


def fill_fields(word, choosen_letter):
    if word.__contains__(choosen_letter):
        for x in word:
            if x == choosen_letter:
                print(x, end="")
            else:
                print("_", end="")


# Deklaracja słowa
print("Wprowadź słowo:")
word_input = input()

game1 = Hangman(word_input)
word_length = game1.count_fields()
print(f"Pola słowa to: {game1.print_fields()}")
print(f"słowo sklada się z {word_length} liter")

number_of_attemps = 11  # bo tyle ruchów potrzeba do narysowania szubienicy i wisielca
print(f"Masz {number_of_attemps} prób")

used_letters = []
counter = 0
word_result = game1.print_fields()
while number_of_attemps > 0:
    print(f"\nUżyte do tej pory litery: {used_letters}")
    print("Podaj literę")
    letter = input()
    if word_input.__contains__(letter):
        print(f"litera {letter} występuje w słowie")
        print("Bieżący status słowa:")
        fill_fields(game1.word, letter)
    else:
        print(f"litera {letter} NIE występuje w słowie")
        number_of_attemps -= 1
        used_letters.append(letter)
        print(f"Pozostało {number_of_attemps} prób")
    counter += 1
