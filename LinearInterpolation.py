"""
1. Wczytanie oryginalnego pliku z częstotliwościami i poziomami napięcia/tłumienia.
2. Wczytanie pliku z częstotliwościami pożądanymi.
3. Zainterpolowanie częsotltiwości nieobecnych w pliku oryginalnym.
"""


def read_original_freq_and_level():
    original_file = open("original_freq_and_level.txt", "r")
    original_frequency = []
    original_level = []
    original_frequency = original_file.readline().split("\t")
    print(f"f = {original_frequency[0]}")


read_original_freq_and_level()
