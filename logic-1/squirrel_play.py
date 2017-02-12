def squirrel_play(temp, is_summer):
  if(is_summer == "yes"):
    return (60 <= temp <= 100)
  else:
    return (60 <= temp <= 90)

temp = input("What is the temperature?: ")
is_summer = raw_input("Is it summer? (yes or no) ")

print(squirrel_play(temp,is_summer))