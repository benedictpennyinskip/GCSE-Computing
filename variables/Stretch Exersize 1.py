#Ben Penny-Inskip
#15-09-2014
#Stretch Exersise 1

length = float(input("Garden Length:"))
width = float(input("Garden width:"))

length = length - 2
width = width -2
answer = length * width
answer = answer * 10

print("It will cost £{0}".format(answer))
