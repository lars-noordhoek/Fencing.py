# description: Fencing price calculator
# Author: Lars Noordhoek
# Date: 26/06/2017
# V1: takes input and gives output
# V2: takes input and gives output and uses function to check for integer input


def get_num_input(prompt):
    input_val = False
    # while the num is not valid do:
    while not input_val:
        # try this
        try:
            num_input = input(prompt)
            # Returns true if string contains only digits and false otherwise.
            if str.isdigit(num_input):
                # sets num val to true
                input_val = True
                # casts string to integer
                return int(num_input)
            else:
                # sets low num val to false
                input_val = False
                # print etc
                print("please enter an integer")
        # excepts value error of input
        except ValueError:
            # print etc
            print("something went wrong that I didn't think of")


price_per_meter = get_num_input("What is the price per meter of fencing? ")
length = get_num_input("What is the length of the paddock? ")
width = get_num_input("What is the width of the paddock? ")

perimeter = (length + width) * 2
estimate = perimeter * price_per_meter
print("We estimate it will cost you ${}".format(estimate), "to fence this paddock.")
