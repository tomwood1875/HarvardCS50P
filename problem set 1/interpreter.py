expression = input("Expression: ")

x, y, z = expression.split()

x = float(x)
z = float(z)

if y == '+':
    result = x+z
elif y == '-':
    result = x-z
elif y == '*':
    result = x*z
elif y == '/':
    result = x/z
else:
    print("Error: Invalid Operator Selected")

print(result)