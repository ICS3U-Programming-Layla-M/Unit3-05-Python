#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 13, 2021
# This program uses a switch statement, asks the user to input
# a number between 1 and 12 and display which month that number
# corresponds to


# switch case equivalent in Python
def month_display(month):

    # checks if number represents a month or not
    months = {
        1: "{} represents January.". format(month),
        2: "{} represents February.". format(month),
        3: "{} represents March.". format(month),
        4: "{} represents April.". format(month),
        5: "{} represents May.". format(month),
        6: "{} represents June.". format(month),
        7: "{} represents July.". format(month),
        8: "{} represents August.". format(month),
        9: "{} represents September.". format(month),
        10: "{} represents October.". format(month),
        11: "{} represents November.". format(month),
        12: "{} represents December.". format(month)
    }

    # error message if the number does not represent a month
    return months.get(month, "{} does not represent a month.". format(month))


# ask user to input a number between 1 and 12
if __name__ == "__main__":
    monthNumber = int(input("Enter a number between 1 and 12: "))
    print(month_display(monthNumber))
