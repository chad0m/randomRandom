from random import randint #just a test TODO: Replace this with random_nums

class ride_the_bus:
	'''give integer 0-int] ace high'''
	def __init__(self) -> None:
		print("Welcome to ride the bus, answer the questions to end the game!")
		print()
		self.cardNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
		self.cardSuits = ['hearts', 'diamonds', 'spades', 'clubs']

	def cardOne(self, round):
		'''round where user guesses the color of the card, input to function is round num'''
		print("Guess the color of the card, enter 'black' or 'red' for your guess:")
		guess  = input("Enter input (ex: red): ")
		possible = ['red', 'black']
		while True:
			correct = randint(0,1) #red 0, black 1
			if guess.lower() == 'red' and correct == 0:
				print("Correct!")
				return True
			elif guess.lower() == 'black' and correct == 1:
				print("Correct!")
				return True
			guess = input(f"Incorrect, it was {possible[correct]}! Enter input: ")
			if round == 1:
				return False

	def cardTwo(self, round):
		'''card where user has to guess higher or lower of card dealt, in is round num'''
		print("Guess if the next card is 'higher', 'lower', or 'same' when compared to the card below")
		card = randint(2, 14)
		print(f"{card}")
		while True:

'''https://en.wikipedia.org/wiki/Around_the_world_(card_game)
https://www.thrillist.com/culture/ride-the-bus-drinking-game

'''


if __name__ == '__main__':
	i = ride_the_bus()
	#round 0
	i.cardOne(0)
	i.cardTwo(0)