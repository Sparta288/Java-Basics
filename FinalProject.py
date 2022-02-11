from ModuleTwo import my_instructions
from ModuleTwo import my_function
# function imported from previous module of code
my_function()
# variables for previous code
firstDistance = 1
optionTwo = 4
print("\nIn order to get home you must follow my directions exactly and acknowledge each set of instructions.\n")
my_function()
print("Drive 15 miles north on the highway.")
print("Turn east on exit 7 and drive for exactly 8km. Take exit 4. You have arrived!")
print("If you pass exit 5 you have gone to far.")
my_function()
# driving directions
optionOne = input("\nWould you like instructions to drive home from Mission Viejo in San Diego?\nType 'yes' or 'no': ")
# user input to receive driving instructions
if optionOne == "yes":
    print("\nDrive for 15 miles.\n")
    while firstDistance != 15:
        firstDistance += 1
        print("Keep driving. You are at mile " + str(firstDistance - 1) + ".")
        if firstDistance == 15:
            print("\nYou are approaching mile 15. Turn east onto exit 7 and drive for 8 miles.")
            optionThree = input("Do you turn east or west? Type 'east' or 'west': ")
            if optionThree == "east":
                print("\nOk good choice, your paying attention.")
                my_instructions()
            elif optionThree == "west":
                while optionThree != "east":
                    print("\nTurn around and go east!\n")
                    optionThree = input("Do you turn east or west? Type 'east' or 'west': ")
                    if optionThree == "east":
                        print("\nGood. You are back on track!")
                        my_instructions()
else:
    print("\nOkay, find your own way home.")






