def make_animal_sound(animal):
    """Returns the sound made by a given animal.

    This function takes the name of an animal as input and returns the corresponding
    sound that the animal makes. If the animal is not recognized, it returns 'unknown sound'.

    Args:
        animal (str): The name of the animal for which the sound is requested.

    Returns:
        str: The sound made by the animal, or 'unknown sound' if the animal is not recognized.
    """

    Created on: January 20, 2025
    """
    sounds = {
        'cat': 'meow',
        'dog': 'woof',
        'cow': 'moo',
        'duck': 'quack'
    }
    return sounds.get(animal.lower(), 'unknown sound')

def get_animal_legs(animal):
    """Gets the number of legs for a given animal.

    Args:
        animal (str): The name of the animal to look up.

    Returns:
        int: The number of legs the animal has. Returns 0 if the animal is not found in the predefined list.

    Created on: January 20, 2025
    """
    legs = {
        'cat': 4,
        'dog': 4,
        'duck': 2,
        'spider': 8
    }
    return legs.get(animal.lower(), 0)

def describe_animal(animal):
    """Provides a description of an animal's sound and number of legs.

    Args:
        animal (str): The name of the animal to describe.

    Returns:
        str: A string describing the sound the animal makes and the number of legs it has.

    The function uses helper functions `make_animal_sound` and `get_animal_legs` to
    retrieve the sound and number of legs for the given animal, respectively.
    """

    Created on: January 20, 2025
    """
    sound = make_animal_sound(animal)
    legs = get_animal_legs(animal)
    return f"A {animal} makes '{sound}' and has {legs} legs!"
