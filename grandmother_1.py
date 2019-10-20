#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to input their age
# and tells them if they can date a granddaughter


def main():
    # This function tells user if they can date a granddaughter

    # input
    number = input("Enter your age: ")
    print("")

    # process
    try:
        age = int(number)

        if (age >= 25 and age <= 40):
            print("You can date my granddaughter.")

        else:
            print("You cannot date my granddaughter.")

    except (ValueError):
        print("Invalid input.")


if __name__ == "__main__":
    main()
