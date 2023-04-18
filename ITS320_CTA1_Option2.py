# method for calculations and printing values
def doMath(user_input1, user_input2):
  int_div = user_input1 // user_input2
  float_div = user_input1 / user_input2
  mod_div = user_input1 % user_input2
  print('Integer division result: ', int_div)
  print('Float division result: ', float_div)
  print('Modulo division result: ', mod_div)


# variables to store user input as float numbers
userInput1 = float(input('Enter first number for division calculations: '))
userInput2 = float(input('Enter second number for division calculations: '))
 
# call function using the variables for user input
doMath(userInput1, userInput2)
