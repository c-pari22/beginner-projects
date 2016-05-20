from random import randint


myfile = open("wof.txt", "r")
lines = myfile.readlines()
myfile.close()

def create_dummy_phrase(phrase):
	new_phrase = []
	for letter in phrase:
		if letter == ' ':
			new_phrase.append(' ')
		elif letter != '\n':
			new_phrase.append("_")
	return new_phrase

def update_dummy(dummy, real, letter):

	for i in range(len(real)):
		if real[i] == letter:
			dummy[i] = letter

def print_dummy(dummy):
	for char in dummy:
		print(char, end="")

def play():
	index = randint(0, len(lines) - 1)
	phrase = lines[index]
	correct = [] 
	wrong = []
	numWrong = 0
	dummyPhrase = create_dummy_phrase(phrase)
	solved = False
	while (not solved and numWrong < 8):
		print_dummy(dummyPhrase)
		print()
		guess = input("Would you like to guess a letter? (y/n)")
		if (guess == 'y'):
			letter = input("What letter would you like to guess? (a-z)")
			if letter in correct or letter in wrong:
				numWrong += 1
				print("You already guessed that!")
			else:
				if letter in phrase:
					update_dummy(dummyPhrase, phrase, letter)
					correct.append(letter)
					if (check_dummy(dummyPhrase, phrase)):
						solved = True
				else:
					print("That's not in the phrase!")
					wrong.append(letter)
					numWrong += 1
		else:
			answer = input("What is your answer to the puzzle? ")
			if (check_dummy(answer, phrase)):
				solved = True
			else:
				numWrong += 1
				print("Sorry thats wrong! Continue on!")
	if (solved):
		print("Congrats you win!")
	else:
		print("The man has been hanged")


def check_dummy(dummy_array, phrase):
	equal = True
	for i in range(0, len(dummy_array)):
		if dummy_array[i] != phrase[i]:
			equal = False
	return equal  



def main():
	playGame = input("Would you like to play Hangman? (y/n)")
	if (playGame == 'y'):
		play()
		main()
	else: 
		print("Now that that's over, wanna know how I got these scars?")


if __name__ == "__main__": main()
 