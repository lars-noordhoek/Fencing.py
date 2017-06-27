# description: Fencing price calculator
# Author: Lars Noordhoek
# Date: 26/06/2017
# V1: takes input and gives output

price_per_meter = int(input("What is the price per meter of fencing? "))
length = int(input("What is the length of the paddock? "))
width = int(input("What is the width of the paddock? "))

perimeter = (length + width) * 2
estimate = perimeter * price_per_meter
print("We estimate it will cost you ${}".format(estimate), "to fence this paddock.")
