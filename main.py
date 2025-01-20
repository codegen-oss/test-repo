from animal_functions import make_animal_sound, get_animal_legs, describe_animal

def main():
    """Main function to test animal-related functions.

    This function prints a welcome message and a separator line. It then tests 
    individual animal functions by printing the sound of a cat and the number of 
    legs a spider has. Finally, it iterates over a list of animals and prints 
    descriptions for each.

    Args:
        None

    Returns:
        None
    """

    Created on: January 20, 2025
    """
    # Test our animal functions
    print("Welcome to the Animal Kingdom!")
    print("-" * 30)
    
    # Test individual functions
    print(f"Cat sound: {make_animal_sound('cat')}")
    print(f"Spider legs: {get_animal_legs('spider')}")
    
    # Test the description function
    animals = ['dog', 'duck', 'cat']
    for animal in animals:
        print(describe_animal(animal))

if __name__ == "__main__":
    main()
