
# Gets invited guests list from file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Gets letter text from file
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()

# Strip the "\n" from the names on the list, puts them into the letter template,
# appends them to the letters list and then writes them to a new txt file
letters = []
index = 0
for name in names:
    names[index] = name.strip("\n")
    letters.append(letter_template.replace("[name]", names[index]))
    with open(f"./Output/ReadyToSend/Letter to {names[index]}", mode="w") as final_letter:
        final_letter.write(letters[index])
    index += 1
