from random import randint #just a test TODO: Replace this with random_nums

class OutOfCards(Exception):
	pass
class ride_the_bus:
	'''give integer 0-int] ace high'''
	def __init__(self) -> None:
		print("Welcome to ride the bus, answer the questions to end the game!")
		print()
		self.drinkCount = 0
		self.cardsDrawn = 0
		self.cardNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
		self.cardSuits = ['hearts', 'diamonds', 'spades', 'clubs']

	def drawCard(self, num):
		if self.cardsDrawn >= 52:
			raise OutOfCards
		else: self.cardsDrawn += 1
		return randint(0,num-1) #non-inclusive to mimic liams function

	def cardOne(self, round):
		'''round where user guesses the color of the card, input to function is round num'''
		print("Guess the color of the card, enter 'black' or 'red' for your guess:")
		possible = ['red', 'black']
		while True:
			guess  = input("Enter guess: ")
			correct = self.drawCard(2) #red 0, black 1
			if guess.lower() == 'red' and correct == 0:
				print("Correct!")
				return True
			elif guess.lower() == 'black' and correct == 1:
				print("Correct!")
				return True
			else: 
				guess = print(f"Incorrect, it was {possible[correct]}!")
				self.drinkCount += 1
				if round == 1:
					return False

	def cardTwo(self, round):
		'''card where user has to guess higher or lower of card dealt, in is round num'''
		print("Guess if the next card is 'higher', 'lower', or 'same' when compared to the card below")
		while True:
			card1 = self.drawCard(13)+2
			print(f"{card1}")
			guess = input("Enter guess: ")
			card2 = self.drawCard(13)+2
			if guess.lower() == 'higher' and card1 < card2:
				print(f"Correct! Card was {card2}")
				return True
			elif guess.lower() == "lower" and card1 > card2:
				print(f"Correct! Card was {card2}")
				return True 
			elif guess.lower() == "same" and card1 == card2:
				print(f"Correct! Card was {card2}")
				return True
			else:
				print(f"Incorrect! Card was {card2}")
				self.drinkCount += 1
				if round == 1:
					return False

	def cardThree(self, round):
		'''card where user has to guess in or out of two cards dealt, in is round num'''
		print("Guess if the next card is 'in', 'out', or 'same' when compared to the two cards below (2-14)")
		while True:
			card0 = self.drawCard(13)+2
			card1 = self.drawCard(13)+2
			print(f"Cards:{card0}, {card1}")
			guess = input("Enter guess: ")
			card2 = self.drawCard(13)+2
			if guess.lower() == 'in' and (card0 < card2 < card1 or card1 < card2 < card0):
				print(f"Correct! Card was {card2}")
				return True
			elif guess.lower() == "out" and (card0 > card2 < card1 or card0 < card2 > card1):
				print(f"Correct! Card was {card2}")
				return True 
			elif guess.lower() == "same" and (card1 == card2 or card0 == card2):
				print(f"Correct! Card was {card2}")
				return True
			else:
				print(f"Incorrect! Card was {card2}")
				self.drinkCount += 1
				if round == 1:
					return False

	def cardFour(self,round):
		"""card where users have to guess the suit, in is round num, out is win-true, lose-false for round 2/1"""
		print("Guess the suit of the next card, possible answers 'clubs', 'diamonds', 'hearts', 'spades'")
		while True:
			guess = input("Enter guess: ")
			card = self.drawCard(4)
			if guess.lower() == self.cardSuits[card]:
				print("Correct!")
				return True
			else:
				print(f"Incorrect, card was {self.cardSuits[card]}!")
				self.drinkCount += 1
				if round == 1:
					return False


'''https://en.wikipedia.org/wiki/Around_the_world_(card_game)
https://www.thrillist.com/culture/ride-the-bus-drinking-game

'''


if __name__ == '__main__':
	i = ride_the_bus()
	#round 0
	try:
		i.cardOne(0)
		i.cardTwo(0)
		i.cardThree(0)
		i.cardFour(0)
	except OutOfCards:
		print("You are out of cards for this round.")
	
	#round 1 - ride the bus
	if input("Would you like to ride the bus (y/n): ").lower() != 'n':
		i.cardsDrawn = 0
		try:
			while True:
				if i.cardOne(1) and i.cardTwo(1) and i.cardThree(1) and i.cardFour(1):
					break
				else:
					print("Try again \n")
		except OutOfCards:
			print("You are out of cards for this round, goodbye.")


	print(f"Congrats, you have finished the game. You ended with {i.drinkCount} drinks!")