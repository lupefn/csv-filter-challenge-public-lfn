import sys, pandas
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
	def validateNames(nameSearch):
		while True:
			name = input("Enter the " + nameSearch + " name to filter by: ")
			if any(char.isdigit() or char == " " for char in name):
				print("Please enter a valid" + nameSearch + " name.")
			else:
				return name.lower().capitalize()
	if c == 1:
		return validateNames("first")
	elif c == 2:
		return validateNames("last")
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
	csvData = pandas.read_csv(pathToCSVData)

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