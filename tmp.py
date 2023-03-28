def fill_fields(word, chosen_letter):
    tmp_word = []
    if word.__contains__(chosen_letter):
        for x in word:
            if x == chosen_letter:
                tmp_word = tmp_word + [x]
                print(tmp_word, end="")
            else:
                tmp_word = tmp_word + ["_"]
                print(tmp_word, end="")



print("Wprowadź słowo")
input_word = input()
while True:
    print("Wprowadź literę")
    input_letter = input()
    fill_fields(input_word, input_letter)
