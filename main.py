from random import seed
from random import randint
print("Random Numbers Generator.")
i = input("enter anything here to randomize: ")
print("Your numbers are: ")
seed(i)
# generate numbers
for _ in range(10):
	value = randint(0, 10)
	print(value)
