#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you if your old enough to vote.

import constants


def main():
    # This is what tells you if your old enough to vote.
    print("")
    print("This program will tell you if you are old enough to vote")

    # Input
    age_of_user = int(input("Input your age: "))

    # Process
    if age_of_user >= constants.AGE_TO_VOTE:
        # Output
        print("")
        print("You are old enough to vote.")
    # Process
    elif age_of_user < constants.AGE_TO_VOTE:
        # Output
        print("")
        print("You aren't old enough to vote. However, you will be able to" \
              "vote in {} years".format(constants.AGE_TO_VOTE - age_of_user))
    # Process
    else:
        # Output
        print("Something went wrong, try again.")


if __name__ == "__main__":
    main()
