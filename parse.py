import sys
import pandas as pd
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
			if any(char.isdigit() or char == " " for char in userInput):
				print("Please enter a valid first name.")
			else:
				return userInput.lower().capitalize()
	elif c == 2:
		while True:
			userInput = input("Enter the last name to filter by: ")
			if any(char.isdigit() or char == " " for char in userInput):
				print("Please enter a valid last name.")
			else:
				return userInput.lower().capitalize()
	else:
		while True:
			try:
				userInput = int(input("Please enter the birthday that you'd like to filter by: "))
				if len(str(userInput)) != 8:
					print("Please enter a valid length DOB.")
				else:
					return userInput
			except ValueError:
				print("Please enter a valid DOB.")
def getFilteredData(csv, choice, validInp):
	if choice == 1:
		filtCSV = csv[(csv.first_name == validInp)]
		return filtCSV
	elif choice == 2:
		filtCSV = csv[(csv.last_name == validInp)]
	else:
		filtCSV = csv[(csv.dob == validInp)]
	return filtCSV.values.tolist()
def main():
	if len(sys.argv) != 2:
		print("USAGE: DIR_TO_CSV_DATA")
		sys.exit()

	pathToCSVData = sys.argv[1]
	csvData = pd.read_csv(pathToCSVData)

	printMenu()
	validChoice = validateChoices()
	validInput = validateInput(validChoice)

	filteredCSV = getFilteredData(csvData, validChoice, validInput)
	if filteredCSV == []:
		print("There were no matches to your input.")
	else:
		print("Here are the following matches to your query (first_name, last_name, dob):")
		for query in filteredCSV:
			print(query)

if __name__ == "__main__":
	main()