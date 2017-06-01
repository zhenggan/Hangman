import random

numGuesses = 0

def chooseNum():

	# generate random number
	lineNumber = random.randint(0, 267700)
	
	# open file to read
	file = open("SOWPODS.txt", "r")

	# read a random line from that file
	for i in range(lineNumber):
		wordString = file.readline()
		wordString = wordString.strip()
		
	answerLength = len(wordString)
	guessField = []
	for i in range(answerLength):
		guessField.append("_")
		
	# close file and print that line
	file.close()
	
	returnList = [wordString, guessField]
	return returnList
	
def userGuess():
	userInput = input("Please enter a guess\n")
	userInput = userInput.upper()
	return userInput
	
def processUserGuess(answer, userInput, guessField):
	answerPositions = []
	for i in range(len(answer)):
		if userInput == answer[i]:
			answerPositions.append(i)
		
	for j in answerPositions:
		guessField[j] = userInput
	
	if not answerPositions:
		return 0
	else:
		return 1
	
		
def compareInputToAnswer(answer, userInput, guessField):
	global numGuesses
	if len(userInput) > 1 :
		if userInput == answer:
			numGuesses += 1
			print("You win!")
			numGuesses = 7
		elif userInput != answer:
			print("You have lost!\n")
			print("The answer was ")
			print(answer)
			numGuesses = 7
			
	if len(userInput) == 1:
		correct = processUserGuess(answer, userInput, guessField)
		if correct == 1:
			print(guessField)
			print ("You have %d guesses" %(6 - numGuesses,))
		elif correct == 0:
			numGuesses += 1
			print(guessField)
			print ("You have %d guesses" %(6 - numGuesses,))
	
	didUserWin = 1
	for i in range(len(guessField)):
		if guessField[i] != answer[i]:
			didUserWin = 0
			break
			
	if didUserWin == 1:
		print("You have won!")
		numGuesses = 7
		
	
answerAndGuessField = chooseNum()
answer = answerAndGuessField[0]
guessField = answerAndGuessField[1]
print(guessField)

while numGuesses < 6:
	userInput = userGuess()
	compareInputToAnswer(answer, userInput, guessField)
	
if numGuesses == 6:
	print("You have lost!\n")
	print("The answer was ")
	print(answer)
	
