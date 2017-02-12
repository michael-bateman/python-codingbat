def alarm_clock(day, vacation):
  if(vacation == "yes"):
    if(1 <= day <= 5):
      return "10:00"
    else:
      return "off"
  
  else:
    if(1 <= day <= 5):
      return "7:00"
    else:
      return "10:00"

day = raw_input("Day of the week - (0 - 7, sunday being 0) ")
vacation = raw_input("On vacation? (yes or no) ")

print(alarm_clock(day,vacation))