# modules to be used...
import csv

# ****** Functions ******

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok !="yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response
# ****** Main Routine ******


# set up Dictionaries

# set up list to hold 'moderniser' ingredients

# Ask user for recipe name and check its not blank
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank and can't contain numbers,",
                        "no")

# Ask user where the recipe is originally from (numbers OK)
source = not_blank("Where is the recipe from? ",
                    "The recipe source can't be blank,",
                    "yes")

# Get serving sizes and scale factor

# Loop for each ingredient...

# Get ingredient amount
# Get ingredient name
# get unit
# convery unit to ml
# convert from ml to g
# put updated ingredient in list