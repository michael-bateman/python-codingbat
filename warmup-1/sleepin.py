def sleep_in(weekday,vacation):
  if(weekday == "no" or vacation == "yes"):
    return True
  else:
  	return False

weekday = raw_input("Is it a weekday? (yes or no) ")
vacation = raw_input("Is it a weekend? (yes or no) ")

print(sleep_in(weekday,vacation))