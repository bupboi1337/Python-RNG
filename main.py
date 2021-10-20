#  PYTHON-RNG
# By Nathaniel Carman, 2021.


# importing stuff
from random import seed                                                                            # import seed
from random import randint                                                                         # import randit
# main code
print("Random Numbers Generator. Generates numbers 1 to 10!")                                      # first line of text you see on screen
randomizer = input("enter anything here to randomize. the more stuff the more random it gets!: ")  # ask for user input for randomizaiton algorithm
print("Your numbers are: ")
seed(randomizer)                                                                                   # get seed to start randomizing and stuff
# generate numbers
for _ in range(10):                                                                                # define the range of numbers
    value = randint(0, 10)
    print(value)                                                                                   # print randomized numbers
    print("thank you for using this program!")                                                     # thank the end user for using this program
