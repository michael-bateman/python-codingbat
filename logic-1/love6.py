def love6(a, b):
  if(a == 6 or b == 6 or (a + b == 6) or (a - b == 6) or (b - a == 6)):
    return True
  else:
    return False

a = input("Enter a number: ")
b = input("Enter a second number: ")

print(love6(a,b))