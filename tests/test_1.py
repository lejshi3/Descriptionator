class Character:
    class Details:
        def __init__(self, name = 'Unnamed', age = 30, sex = 'male', expression = 'neutral', profession = 'profession'):
            self.name = name
            self.age = age
            self.sex = sex
            self.expression = expression
            self.profession = profession
        
    class Appearance:
        def __init__(self) -> None:
            pass

        class Skin:
            def __init__(self, color, traits):
                self.color = color
                self.traits = traits

        class Eyes:
            def __init__(self, color, traits):
                self.color = color
                self.traits = traits

        class Eyes:
            def __init__(self, color, traits):
                self.color = color
                self.traits = traits

    class Clothing:
        def __init__(self, attire, accessories):
            self.attire = attire
            self.accessories = accessories

    class Style:
        def __init__(self, style):
            self.style = style

# Create a list of characters
characters = []

# Ask the user how many characters they want to create
num = int(input("How many characters do you want to create? "))

# Loop through the number of characters
for i in range(num):
    # Create a new character instance
    character = Character()

    # Ask the user to enter the name and sex of the character
    character.Details.name = input("Enter the name of the character: ")
    character.Details.sex = input("Enter the sex of the character: ")

    # Add the character to the list
    characters.append(character)

# Print the list of characters
for character in characters:
    print(character.Details.name)
    print(character.Details.sex)
    print()