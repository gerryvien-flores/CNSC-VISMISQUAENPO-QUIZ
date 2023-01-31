#!/usr/bin/python3

def collectAns(num, answer):
	with open("sauce/Answer.txt", "a") as Sheet:
		Sheet.write(num + answer + "\n")

def showQuiz(number):
	with open("sauce/quiz.txt", "r") as Quiz:
		myLines = Quiz.readlines()[number - 1]
		print(myLines)

	with open("sauce/choices.txt", "r") as choices:
		lines = choices.readlines()[number - 1]
		for line in lines.split("~"):
			print(line)

def tallyScore():
	score = 0
	with open("sauce/Answer.txt", "r") as sheet:
		answers = sheet.readlines()

	with open("sauce/key.txt") as correction:
		for lines in correction:
			if lines in answers:
				score += 1

	return score


def tallyMistakes():
	mistakes = []
	with open("sauce/Answer.txt", "r") as sheet:
		answers = sheet.readlines()

	with open("sauce/key.txt") as correction:
		for lines in correction:
			if lines not in answers:
				mistakes.append(lines[0:2].replace('.', ' '))

	return mistakes

def generateResult(name, yrblk, date, score, mistake):
	with open("sauce/Answer.txt", "r") as sheet:
		lines = sheet.readlines()

	with open(f"Result/{name}.txt", "w") as result:
		result.write(f"Name: {name}\nCourse, Year and Block: {yrblk}\nDate: {date}\nScore: {score}\n\n")
		for ans in lines:
			result.write(f"{ans}")

		result.write("\nMistakes:\n")
		for miss in mistake:
			result.write(f"{miss.strip()}\n")

	print("Report had been generated.")



if __name__ == "__main__":
	Sheet = open("sauce/Answer.txt", "w")
	Sheet.truncate(0)
	Sheet.close()

	print('''
		WELCOME TO CNSC VISMISQUAENPO QUIZ

			Options:
				A - Take Quiz
				B - Show Result
				C - Quit
		''')
	while True:
		query = input("Choice: ").casefold()

		if query == "a":
			answeredNums = []
			answered = 0
			studName = input('Name: ')
			yearBlk = input("Course, Year and Block: ")
			dates = input("Date: ")
			while True:
				item = input('Select a number from 1 to 20: ')
				try:
					if item not in answeredNums:
						answeredNums.append(item)
						showQuiz(int(item))
						itemNum = item + ". "
						myAnswer = input(itemNum)
						answered += 1
						collectAns(itemNum,myAnswer)
					else:
						print("You've already answered this number.")

					if answered == 20:
						generateResult(studName, yearBlk, dates, tallyScore(), tallyMistakes())
						break

				except (ValueError, IndexError):
					print("Invalid Option")
		elif query == "b":
			try:
				fileName = input("Please write your name: ") + ".txt"
				with open(f"Result/{fileName}", "r") as resultFile:
					for data in resultFile:
						print(data)
			except FileNotFoundError:
				print("Cannot find test record.")
		elif query == "c":
			print("Thank you for using the application.")
			break
		else:
			print("Unknown Option.")







