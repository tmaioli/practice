# Project Title:Number of Pizza's
# Version: 1.0
# Instructions:
# Built with: Python 3.7
# Coded on: Atom text editor
# Thomas Maioli
# date 2019-02-20
# Project name: Pizza's
# Issues and concerns: none
# Problem domain: Solve poker night Problem
# Keep your code & powder dry.
#
# Variables:
# number_of_people  - int                // input  Number_of_people = int(input(Number of people: "))
# number_of_slices_person - float        // input  Number_of_slices_person = int(input("Number of slices per person: "))
# slices_per_pie - float                 // input  Slices_per_pie = int(input("Slices per pie: "))
# pizzas_needed - int                    // = ceil( (number_of_people * Number_of_slices_person) / slices_per_pie)
# slices_left - int                      // = (pizzas_needed * slices_per_pie)%(number_of_people * number_of_slices_person)
#
#


def main():
    number_of_people = int(input("Number of people: "))
    number_of_slices_person = int(input("Number of slices per person: "))
    slices_per_pie = int(input("Slices per pie: "))
    pizzas_needed = ((number_of_people * number_of_slices_person) / slices_per_pie)
    slices_left = (pizzas_needed * slices_per_pie)%(number_of_people * number_of_slices_person)
    print("You will need " + str(pizzas_needed) + " pizzas to feed " + str(number_of_people)+ ".")
    print("There will be " + str(slices_left) + " leftover slices.")

main()
