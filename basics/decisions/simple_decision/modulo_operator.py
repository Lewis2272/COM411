print("Please enter a whole number")
number = int(input())

if number % 2 == 0:
  print("The number" ,number, "is an even number") 
else:
  print("The number" ,number, "is an odd number") 

#Alternative print function could be
  #print("{} is even".format(number))