import sys
validChoices = [1,2,3]
def printMenu():
	print("By what category would you like to filter the data by?")
	print("1) First name")
	print("2) Last name")
	print("3) Birthday")
def validateChoices():
	while True:
		try:
			userChoice = int(input("Enter your choice: "))
			if userChoice in validChoices:
				break
			else:
				print("Your choice was not a listed one.")
		except ValueError:
			print("Your choice was invalid. Please enter an integer value.")
	return userChoice
def validateInput(c):
	if c == 1:
		while True:
			userInput = input("Enter the first name to filter by: ")
			if any(char.isdigit() for char in userInput):
				print("Please enter a valid first name.")
			else:
				return userInput
	elif c == 2:
		while True:
			userInput = input("Enter the last name to filter by:")
			if any(char.isdigit() for char in userInput):
				print("Please enter a valid last name.")
			else:
				return userInput
	else:
		while True:
			try:
				userInput = int(input("Please enter the birthday that you'd like to filter by."))
				if len(str(userInput)) != 8:
					print("Please enter a valid length DOB.")
				else:
					return userInput
			except ValueError:
				print("Please enter a valid DOB.")

def main():
	if len(sys.argv) != 2:
		print("USAGE: DIR_TO_CSV_DATA")
		sys.exit()

	pathToCSVData = sys.argv[1]
	with open(pathToCSVData) as file:
		lines = file.read().split("\n")

	printMenu()
	validChoice = validateChoices()



if __name__ == "__main__":
	main()