def front3(str):
  if(len(str) <= 3):
    front = str
  else:
    front = str[:3]
  
  return (front * 3)

str = raw_input("Enter a string: ")

print(front3(str))