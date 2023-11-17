"""
1. Wczytanie oryginalnego pliku z częstotliwościami i poziomami napięcia/tłumienia.
2. Wczytanie pliku z częstotliwościami pożądanymi.
3. Zainterpolowanie częsotltiwości nieobecnych w pliku oryginalnym.
"""


def read_original_freq_and_level():
    original_file = open("original_freq_and_level.txt", "r")
    original_frequency = []
    original_level = []
    tmp = original_file.readlines()
    # print(f"TMP: {tmp}")
    for x in range(0, len(tmp)):
        # print(tmp[x])
        original_frequency.append(float(tmp[x].split("\t")[0]))
        original_level.append(float(tmp[x].split("\t")[1].replace(",", ".")))
    print(f"Oryginalne częstotliwości: {original_frequency}")
    print(f"Oryginalne poziomy: {original_level}")


read_original_freq_and_level()
