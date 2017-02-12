def makes10(a, b):
  if(a + b == 10 or a == 10 or b == 10):
    return True
  else:
    return False

a = input("Enter a number: ")
b = input("Enter a second number: ")

print(makes10(a,b))