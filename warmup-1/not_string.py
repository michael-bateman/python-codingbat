def not_string(str):
  if(str[:3] == "not"):
    return (str)
  else:
    return ("not " + str)

str = raw_input("Enter a string: ")

print(not_string(str))