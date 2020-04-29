#Simple Calculator
num1 = int(input("Welcome! \nPlease enter a number: "))
num2 = int(input("Please enter another one: "))
operation = input("What operation would you like to perform? ")

if operation == "*":
  print("The result is ",num1 * num2)

elif operation == "/":

  if num2 == 0:
    print("Error!") 
  else:
    print("The result is %.2f"%(num1 / num2))

elif operation == "+":
  print("The result is ",num1 + num2)

elif operation == "-":
  print("The result is ",num1 - num2)

print("\nThank you for using calculator!")  

