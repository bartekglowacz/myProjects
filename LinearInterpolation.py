"""
1. Wczytanie oryginalnego pliku z częstotliwościami i poziomami napięcia/tłumienia.
2. Wczytanie pliku z częstotliwościami pożądanymi.
3. Zainterpolowanie częsotltiwości nieobecnych w pliku oryginalnym.

wzór na interpolację liniową:
y = (y1-y2)(x-x1)/(x1-x2) + y1
"""


def read_original_freq_and_level(name_of_file):
    original_file = open(name_of_file, "r")
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


# def new_frequencies_file(name_of_file):


read_original_freq_and_level("original_freq_and_level.txt")
