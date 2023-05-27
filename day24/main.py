#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#saving the name of the persons who will be invited
with open("invited_names.txt") as file:
    names = [line.rstrip() for line in file]

#saving the example letter
with open("starting_letter.txt") as starting_letter:
    example_letter = [line.rstrip() for line in starting_letter]

#creating the letters for each person who will be invited
for name in names:
    with open(f"Letters/{name.lower()}_letter.txt", mode="w") as letter:
        #filling the new letter as the example letter
        for line in example_letter:
            if "[name]" in line:
                letter.write(line.replace("[name],", name + ", \n"))
            else:
                letter.write(line + "\n")
