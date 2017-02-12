def monkey_trouble(a_smile, b_smile):
  if(a_smile == "yes" and b_smile == "yes" or a_smile == "no" and b_smile == "no"):
    return True
  else:
    return False

a_smile = raw_input("Is a smiling? (yes or no) ")
b_smile = raw_input("Is b smiling? (yes or no) ")

print(monkey_trouble(a_smile,b_smile))