f = open("alphabet.txt","r")
number = int(input("How many lines of letters would you like?))
for x in range(number):
  print (f.readline())
