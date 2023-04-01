def display_word(secret_word):
    display = ""
    print(f"Beginning: {display}")
    for letter in secret_word:
        if letter in secret_word:
            display += letter
            print(display)
        else:
            display += "_"
            print(display)
    print(display)


word_input = input("Wprowadź słowo: ").lower()
display_word(word_input)
