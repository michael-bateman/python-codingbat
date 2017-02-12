def pos_neg(a, b, negative):
  if(negative == "yes"):
    return (a < 0 and b < 0)
  else:
    return ((a < 0 or b < 0) and (a > 0 or b > 0))

a = input("Enter a number: ")
b = input("Enter a second number: ")
negative = input("Is it negative? (yes or no) ")