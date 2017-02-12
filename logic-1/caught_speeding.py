def caught_speeding(speed, is_birthday):
  speed0 = 60
  speed1 = 61
  speed2 = 81
  
  if(is_birthday == "yes"):
    speed0 = speed0 + 5
    speed1 = speed1 + 5
    speed2 = speed2 + 5
  
  if(speed <= speed0):
    return 0
  elif(speed1 <= speed < speed2):
    return 1
  elif(speed2 <= speed):
    return 2

speed = input("What is your speed? ")
is_birthday = raw_input("Is it your birthday? (yes or no) ")

print(caught_speeding(speed,is_birthday))