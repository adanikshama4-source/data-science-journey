def calculator():
  print("<==Simple Calculator==>")
  while True:
    num1 = input("Enter first number:")
    if num1.lower() == "quit" or num1.lower() == "exit":
      print("Exiting the calculator.")
      break
    else:
      num1 = float(num1)
    num2 = float(input("Enter second number:"))
    operator = input("Enter operator (+,-,*,/):")
  
    if operator == "+":
      result = num1 + num2
    elif operator == "-":
      result = num1  - num2
    elif operator == "*":
      result = num1*num2
    elif operator == "/":
      if num2==0:
        print("Error: Cannot divide by zero!")
      else:
        result = num1/num2
    else:
      result = "Invalid Operation!"
    if result is not None:
      print("Result: ", result)
      print("-"*30)

calculator()
