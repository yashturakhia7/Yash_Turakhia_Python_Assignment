#Write a program that prints the numbers from 1 to 100 and for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”. 

#Fizzbuzz problem
for i in range(1,101):
  if i%3 == 0 and i%5==0:
    print("fizzbuzz")
  elif i%5 == 0:
    print("buzz")
  elif i%3 == 0:
    print("fizz")
  else:
    print(i)
