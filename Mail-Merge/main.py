with open("Mail_Merge_Project_Start/Input/Letters/starting_letter.txt") as data:
    letter = str(data.read())

with open("Mail_Merge_Project_Start/Input/Names/invited_names.txt") as all_names:
    names = all_names.readlines()

for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open(f"Mail_Merge_Project_Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)