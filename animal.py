class AnimalDrawer:
    def __init__(self):
        self.animals = {
            "1": "Dog",
            "2": "Cat",
            "3": "Fish",
            "4": "Elephant",  # Added Elephant
            # Add more animals and their ASCII art here
        }

    def display_animal_list(self):
        print("Choose an animal to draw:")
        for key, value in self.animals.items():
            print(f"{key}. {value}")

    def draw_animal(self, choice):
        animal_name = self.animals.get(choice)
        if animal_name:
            print(f"Drawing {animal_name}:")
            self.draw_specific_animal(animal_name)
        else:
            print("Invalid choice. Please choose a valid animal.")

    def draw_specific_animal(self, animal_name):
        if animal_name == "Dog":
            print("""
 / \\__
(    @\\____
 /         O
/   (_____/
/_____/   U
""")
        elif animal_name == "Cat":
            print("""
 /\\_/\\
( o.o )
 > ^ <
""")
        elif animal_name == "Fish":
            print("""
><(((('> 
""")
        elif animal_name == "Elephant":
            print("""
     __
   /   \\
  /     \\
 ( O   O )
  \\  ∼  /
   | ∼ |
   || ||
""")
        # Add more ASCII art for other animals as needed

    def start_drawing(self):
        self.display_animal_list()
        choice = input("Enter the number of the animal you want to draw: ")
        self.draw_animal(choice)

# Example usage:
if __name__ == "__main__":
    drawer = AnimalDrawer()
    drawer.start_drawing()
