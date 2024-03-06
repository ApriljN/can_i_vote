'''
Can I vote
By April
07/03/2024
Version 1.0
'''

age = int(input("Age: "))
name = input("Name: ")
res = input("Are you a resident of NZ? ")
if age >= 18 and res == "yes":
  print("Hello " + name + ", you are eligible to vote. ")
else:
  print("Sorry " + name + ", you are not eligible to vote.")