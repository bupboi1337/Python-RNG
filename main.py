# importing stuff
from random import seed
from random import randint
# main code
print("Random Numbers Generator. Generates numbers 1 to 10!")
randomizer = input("enter anything here to randomize. the more stuff the more random it gets!: ")
print("Your numbers are: ")
seed(randomizer)
# generate numbers
for _ in range(10):
	value = randint(0, 10)
	print(value)
