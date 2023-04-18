# CTA3 Option 1

# Method for validating digit only input
def ValidateIntInput(): 
    val = False
    userInput = input('Enter a year to evaluate for the Ferrari 250 GTO: ')
    while val is False: 
        if userInput.isdigit() is False:
            print('Invalid input, ensure all characters are digits.')
            userInput = input('Try again: ')
        else:
            val = True
            return userInput

# Method for determining the key for the price dictionary
# Note: This could be rewritten as a match/case scenario
def DetermineKey (userInput): 
    userInput = int(userInput)
    # Value returned from method
    decisionKey = 0 

    # Decision Cases for Key retrieval 
    if 1962 <= userInput <= 1964: 
        decisionKey = 1
    
    elif 1965 <= userInput <= 1968: 
        decisionKey = 2
    
    elif 1969 <= userInput <= 1971: 
        decisionKey = 3
    
    elif 1972 <= userInput <= 1975: 
        decisionKey = 4

    elif 1976 <= userInput <= 1980: 
        decisionKey = 5

    elif 1981 <= userInput <= 1985: 
        decisionKey = 6

    elif 1986 <= userInput <= 2012: 
        decisionKey = 7

    elif 2013 <= userInput <= 2014: 
        decisionKey = 8

    else:
        decisionKey = 0

    return decisionKey

# Collecting User Input
userInput = ValidateIntInput()

# Use DetermineKey method for yielding a key for dict
priceKey = DetermineKey(userInput)

# Dictionary for organzing the price ranges
priceDict = {
    0 : 'Unable to determine value from the input...',
    1 : 18500,
    2 : 6000,
    3 : 12000,
    4 : 48000,
    5 : 200000,
    6 : 650000,
    7 : 35000000,
    8 : 52000000
}

print('The value is: ', priceDict[priceKey])