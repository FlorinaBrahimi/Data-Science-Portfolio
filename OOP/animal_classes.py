class Cat:
    def __init__(self, name, age):
        """
        Initializes the Cat instance with a specified name and age.

        :param name: The name of the cat
        :param age: The age of the cat
        """
        self.name = name  # Set the name attribute for the Cat object
        self.age = age  # Set the age attribute for the Cat object

    def info(self):
        """Displays the cat's name and age."""
        print('My name is ' + self.name + '. My age is ' + str(self.age))  # Print cat info

    def make_sound(self):
        """Makes the sound typical of a cat."""
        print('mew mew')  # Print cat sound


class Dog:
    def __init__(self, name, age):
        """
        Initializes the Dog instance with a specified name and age.

        :param name: The name of the dog
        :param age: The age of the dog
        """
        self.name = name  # Set the name attribute for the Dog object
        self.age = age  # Set the age attribute for the Dog object

    def info(self):
        """Displays the dog's name and age."""
        print('My name is ' + self.name + '. My age is ' + str(self.age))  # Print dog info

    def make_sound(self):
        """Makes the sound typical of a dog."""
        print('bow wow')  # Print dog sound


def my_pet(pet):
    """
    Interacts with a pet by displaying its info and sound.

    :param pet: An instance of either Cat or Dog
    """
    pet.info()  # Call the info method of the pet
    pet.make_sound()  # Call the make_sound method of the pet


# Create instances of the Cat and Dog classes with specific names and ages
c = Cat('Kitty', 2)
d = Dog('Tommy', 3)

# Interact with the dog instance
my_pet(d)  # Call the my_pet function with the dog instance
