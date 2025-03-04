#!/usr/bin/env python3
# Created by: Gustav Ihlenfeld
# Created on: March 4, 2025
# This program asks the user for the diameter of the
# pizza. It calculates and displays the total cost
# of the pizza along with tax
import constants

def main():
    # input
    diameter = int(input("Please enter the diameter of the pizza (inches): "))

    # process
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("The total cost is ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
