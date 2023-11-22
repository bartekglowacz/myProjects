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
        original_frequency.append(float(tmp[x].split("\t")[0].replace(",", ".")))
        original_level.append(float(tmp[x].split("\t")[1].replace(",", ".")))
    # print(f"Oryginalne częstotliwości: {original_frequency}")
    # print(f"Oryginalne poziomy: {original_level}")
    return [original_frequency, original_level]


def desired_freq(name_of_file):
    original_file = open(name_of_file, "r")
    desired_frequencies = []
    tmp = original_file.readlines()
    # print(f"TMP: {tmp}")
    for x in range(0, len(tmp)):
        desired_frequencies.append(float(tmp[x].replace(",", ".")))
    return desired_frequencies


def interpolate(original_frequency, original_level, desired_frequencies):
    interp_level = []
    for x in range(0, len(desired_frequencies)):
        try:
            # print(f"I element oryginalnej częstotliwości to {original_frequency[x]}")
            # print(f"II element oryginalnej częstotliwości to {original_frequency[x + 1]}")
            # print(f"I element oryginalnego poziomu to {original_level[x]}")
            # print(f"II element oryginalnego poziomu to {original_level[x + 1]}")
            y = (original_level[x] - original_level[x + 1]) * (desired_frequencies[x] - original_frequency[x]) / (
                        original_frequency[x] - original_frequency[x + 1]) + original_level[x]
            interp_level.append(float(y))
        except Exception:
            break
    return [desired_frequencies, interp_level]


a = read_original_freq_and_level("original_freq_and_level.txt")[0]
b = read_original_freq_and_level("original_freq_and_level.txt")[1]
c = desired_freq("desired_frequencies.txt")
d = interpolate(a, b, c)

print(f"a wynosi {a}\nb wynosi {b}\nc wynosi {c}\n")
print("test: ", interpolate(a, b, c))
