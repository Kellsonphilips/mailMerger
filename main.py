# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as all_names:
    names = all_names.readlines()


with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    invitation = starting_letter.read()
    for name in names:
        striped_names = name.strip("\n")
        new = invitation.replace(PLACE_HOLDER, striped_names)
        with open(f"./Output/ReadyToSend/letter_to_{striped_names}.txt", "w") as new_letters:
            new_letters.write(new)
    print(new)
