# This is where we declare the values for the tickets and discounts
coachTic = 199
firstClassTic = 500
seniors = .20
seniorAge = 65
kids = .20
kidAge = 7

# This is where we need to do the inputs for passenger and ticket info into an array
quantity = input("Hello and welcome to Chaffey Airlines. How many tickets will you be purchasing today? ")
#travdata SMM
year = 0
minMonth = 1
maxMonth = 12
minDay = 1
maxDay = 31
numTravelers = 0
i = 1
prefClass = ("","First Class" ,"Coach")
travDestination = ("","FL", "CA", "NY","TX", "VA")

#date and number of traveilers 
year = int(input("Enter travel year: "))
month = int(input("Enter travel month: ")) 
day = int(input("Enter travel day: "))
numTravelers = int(input("Enter number of travelers: "))
travelDes = int(input("Travel destination- 1-FL, 2-CA, 3-NY, 4-TX, 5-VA: "))

travDate = str(print("Travel Date is: ", month,"/",day,"/",year))

while i <= numTravelers:
  travName = str(input ("What is the traveler's Name: "))
  travAge = str(input("Age of travelers: "))
  prefClass1 = int(input ("Preferred Class- 1 First Class or 2 Coach: "))
  i = i +1

  print ("Traveler", travName)
  print ("Traveling", prefClass[prefClass1])
  print ("Traveling to", travDestination[travelDes])
#SMM

# This is the table that needs to be somehow put into an array

fc= "First Class"
ch= "Coach"
fcRow1 = "Row FCA"
fcRow2 = "Row FCB"
row1 = "Row A"
row2 = "Row B"
row3 = "Row C"
row4 = "Row D"
opA = "A Open"
opB = "B Open"
opC = "C Open"
opD = "D Open"


print ("========== %s ========== \n            | %-5s| %-5s|" %(fc, fcRow1,fcRow2))

for i in range(4):
  print("FC seats %d" %(i), end =" ")
  print(" | %-5s | %-5s |" %(opA, opB))


print("**********************************************************************************")

print ("========== %s ========== \n         |  %-5s |  %-5s |  %-5s |  %-5s |" %(ch, row1,row2,row3,row4))

for i in range(10):
  print("seats %d" %(i), end =" ")
  print(" | %-5s | %-5s | %-5s | %-5s |" %(opA, opB, opC, opD))

fileName = input("what file name do you want to create? ")
import os
if os.path.exists(fileName):
  print("file exists!")

f = open(fileName, "x")

f = open(fileName, "a")

f = open(fileName, "r")
print(f.read())
f.close()
# here is where we manipulate the array


# This is where we let passengers make changes to array


# This is where we give totals for ticket prices and verification of seats that might loop back to making changes


#This is where we checkout and make change based on total
