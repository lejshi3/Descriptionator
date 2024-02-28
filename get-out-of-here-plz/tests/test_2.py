class Character:
    class Details:
        def __init__(self, name = 'Unnamed', age = 30, sex = 'male'):
            self.name = name
            self.age = age
            self.sex = sex
        

# Create a list of characters
characters = []

# Ask the user how many characters they want to create
num = int(input("How many characters do you want to create? "))

# Loop through the number of characters
for i in range(num):
    # Get character details from the user
    name = input("Enter the name of the character: ")
    age = int(input("Enter the age of the character: "))
    sex = input("Enter the sex of the character: ")

    # Create a new Character object and add it to the list
    new_character = Character()
    new_character.Details = new_character.Details(name, age, sex)
    characters.append(new_character)

# Print the character information
for character in characters:
    print(f"{character.Details.name}, a {character.Details.age}yo {character.Details.sex}")