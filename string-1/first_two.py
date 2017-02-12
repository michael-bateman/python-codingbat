def first_two(str):
  if (str <= 2):
    return str
  else:
    str = str[:2]
    return str

str = raw_input("Enter a string: ")

print(first_two(str))