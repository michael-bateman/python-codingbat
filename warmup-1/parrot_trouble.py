def parrot_trouble(talking, hour):
  if(talking == "yes" and (hour < 7 or hour > 20)):
    return True
  else:
    return False

talking = raw_input("Is it talking? (yes or no) ")
hour = input("What time is it? (ex. 4) ")

print(parrot_trouble(talking,hour))