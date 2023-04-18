# ITS320_CT2_Option1

# Method: Validation that input is <= 50
def ValidateInput(userInput, inputLength): 
  val = False
  # While loop for checking input for max of 50 chars
  while val is False: 
    if inputLength > 50: 
      userInput = input('The string is too long, try again: ')
      inputLength = len(userInput)
    else: 
      val = True

# Methods for String analysis method in order to return Boolean
def AlnumDetection(userInput):
  return any(i.isalnum() for i in userInput)

def AlphaDetection(userInput):
  return any(i.isalpha() for i in userInput)

def DigitDetection(userInput): 
  return any(i.isdigit() for i in userInput)

def LowerDetection(userInput):
  return any(i.islower() for i in userInput)

def UpperDetection(userInput):
  return any(i.isupper() for i in userInput)

# Method for compiling prior methods into a single method
def StringAnalysis(userInput):
  # Variables used to store detection from detectiong methods
  alnumDetect = AlnumDetection(userInput)
  alphaDetect = AlphaDetection(userInput)
  digitDetect = DigitDetection(userInput)
  lowerDetect = LowerDetection(userInput)
  upperDetect = UpperDetection(userInput)

  # Print Functions
  print('Detection of alphanumeric characters: ', alnumDetect)
  print('Detection of alphabetical characters: ', alphaDetect)
  print('Detection of digit characters: ', digitDetect)
  print('Detection of lowercase characters: ', lowerDetect)
  print('Detection of uppercase characters: ', upperDetect)
  

# Variable for user String and length of String
S = input('Enter a string to determine the presence of specific characters: ')
sLength = len(S)

# Calling of defined methods onto the user string
ValidateInput(S, sLength)
StringAnalysis(S)