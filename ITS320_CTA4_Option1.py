# CTA for Module 4

# method for testing float input
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Method for validating input
def ValidateFloat():
    val = False
    userInput = input('Enter a float number to add to the list: ')
    while val is False:
        if isfloat(userInput) is False:
            print('Invalid input, ensure input is a float.')
            userInput = input('Try again: ')
        else:
            val = True
            return float(userInput)

# method for sum of list elements
def SumOfList(userList):
    total = 0
    for i in range(0, len(userList)):
        total = total + userList[i]
        i = i + 1 
    return total

# method for average of the list
def AverageOfList(userList):
    total = SumOfList(userList)
    average = total / len(userList)
    print('The average of the list:', average)

# method for finding the interest of each list element
def FindInterestValue(userList):
    for i in range(0,len(userList)):
        interestValue = userList[i] + (userList[i] * 0.2)
        print('Original Value for ', i, ': ', userList[i])
        print('Interest Value for ', i, ': ', interestValue)
        i = i + 1 

# running methods
# start with accepting input from the user using a for loop
inputList = []
for i in range(0,5):
    addInput = ValidateFloat()
    inputList.append(addInput)
    i = i + 1

# display sum of list
inputSum = SumOfList(inputList)
print('Sum of the input values: ', inputSum)

# method for displaying average of list
AverageOfList(inputList)

# display the max of the list
print('The maximum of the list: ', max(inputList))

# display the min of the list
print('The minimum of the list: ', min(inputList))

# method for displaying the interest values with the origianl value
FindInterestValue(inputList)
