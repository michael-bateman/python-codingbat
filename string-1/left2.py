def left2(str):
  if(len(str) <= 2):
    return str
  else:
    strfirst = str[:2]
    strend = str[2:]
    return strend + strfirst

str = raw_input("Enter a string: ")

print(left2(str))