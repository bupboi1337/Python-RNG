# PYTHON-RNG
# By Nathaniel Carman, 2021.


# Importing Librarys
from random import seed
from random import randint
# Main code
print("Random Numbers Generator. Generates numbers 1 to 10!")                                      # First line of text you see on screen
randomizer = input("enter anything here to randomize. the more stuff the more random it gets!: ")  # Ask for user input for randomizaiton algorithm
print("Your numbers are: ")
# Generate results
seed(randomizer)                                                                                   # Get seed to start randomizing
for _ in range(10):                                                                                # Define the range of numbers
    value = randint(0, 10)
    print(value)                                                                                   # Print randomized numbers
    print("thank you for using this program!")                                                     # Thank the End User for using this program
