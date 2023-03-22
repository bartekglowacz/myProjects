def fill_fields(word, letter):
    if word.__contains__(letter):
        for x in word:
            if x == letter:
                print(x, end="")
            else:
                print("_", end="")


print("Wprowadź słowo")
input_word = input()
print("Wprowadź literę")
input_letter = input()
fields_input = "_" * len(input_word)
print(fields_input)
fill_fields(input_word, input_letter)

