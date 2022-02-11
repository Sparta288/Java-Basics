# print("Welcome to my roller-coaster!")
# # user choice to ride roller=coaster
# userChoice = str(input("\nWould you like to ride?\nType Y for Yes and N for No: "))
# # user enters age if yes
# def roller_coaster():
#  userAge = 0
#  userHeight = 0
#
#
#  while userAge < 12 and userHeight <= 130:
#
#     if userChoice == "y" or "yes" or "YES" or "Yes":
#         userAge = int(input("\nGreat! Enter your age: "))
#         # if users age is 12 or older user can continue
#         if userAge >= 12:
#             # user enters height
#             userHeight = int(input("\nEnter your height in cm: "))
#             if userHeight >= 130:
#                 print("\nCongrats, you meet the requirements to ride the roller-coaster!")
#             # user is not tall enough
#             else:
#                 print("\nSorry, you must be at least 130cm tall to ride the roller-coaster.")
#
#
#         else:
#             print("\nSorry, you must be at least 12 years of age or older to ride the roller-coaster. ")
#
#         # user choose not to ride roller-coater
#     else:
#         print("\nOk, Have a nice day!")





# print("Would you like directions to get downtown?\n")
# userAnswer = str(input("Enter 'y' for yes and 'n' for no:"))
# if userAnswer == "y":
#     travelOption = str(input("Would you like to drive or walk to get downtown? Enter 'w' for walk and 'v' for vehicle: "))
#     if travelOption == "v":
#         print("Ok, great. Face North and walk 1/4 of a mile to the parking lot.")
#         direction = str(input("Would you like to go left or right? : Enter 'r' for right and 'l' for left: "))
#         if direction == "r":
#             print("You turned right onto Enterprise street. Drive on this street for 10 miles until you reach exit 31.")
#             choice = str(input("Would you like to take a right or left?: "))
#             if choice == "left":
#                 print("You have arrived downtown in 1 hour!")
#             elif choice == "right":
#                 print("Wrong way go left")
#         elif direction == "l":
#             print("You turned left on Enterprise street. Take a right onto Lagoon Street and drive for 10 miles.\n")
#             print("Take exit 31 and turn left. You have arrived in 1 hour and 30 minutes!")
#     elif travelOption == "w":
#         print("You chose to walk. Face North and walk 1/4 mile towards the parking lot.")
#         print("Walk East to Enterprise street.")
#         walkChoice = str(input("Would you like to walk or ride the train? Type 't' for train and 'w' for walk: "))
#         if walkChoice == "t":
#             print("Get on train. Get off at second stop. You have arrived downtown in 20 minutes!")
#         elif travelOption == "w":
#             print("Walk for 10 miles on Enterprise road")
#             print("Get off at exit 31.\nTake a left after the exit.\n You have arrived downtown 12 hours later!")
#
# else:
#     print("Ok, have a great day!")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# totalDateMoney = 150
# superHeroMovie = 65
# daVinciRestaurant = 132
# shakesSpearePlay = 45
# starLightLanes = 30
# hotDog = 15 # per person
# tenGuysBurgers = 12 # per person
# sushi = 40 # per person
# moonLightBoat = 35 # each person
#
#
# print("You have a date tonight but you only have 150 dollars to spend. "
#       "There are lots of things to do so use the money wisely. ")
#
# ChoiceOne = input("\nDo you want to go to dinner or a movie first? Type dinner or movie : ")
# if ChoiceOne == "dinner":
#     ChoiceTwo = input("\nWhere would you like to go out to eat? "
#     "The local DaVinci Ristorante is serving the town's best food\nor "
#     "Fukiyama Sushi does an all-you-can-eat sushi buffet. Type davinci or sushi:  ")
#     if ChoiceTwo == "davinci":
#         totalDateMoney = totalDateMoney - daVinciRestaurant
#         print("You had a great dinner. You only have " + str(totalDateMoney) + " dollars remaining. You don't have enough money"
#                                                                                                  " to continue the date. You go home.")
#
#     else:
#         totalDateMoney = totalDateMoney - sushi
#         ChoiceThree = input("\nYou had sushi and it was good. Your have " + str(totalDateMoney) + " dollars remaining. "
#         "Time for a movie.\nThe latest large-screen film presentation of the hot blockbuster superhero movie is playing at 7 p.m.\n"
#         "Do you go to the movie? Type yes or no : ")
#         if ChoiceThree == "yes":
#                 totalDateMoney = totalDateMoney - superHeroMovie
#                 print("You enjoyed the movie and have " + str(totalDateMoney) + " dollars remaining.")
#                 ChoiceFour = input("Do you want to go bowling? Type yes or no : ")
#                 if ChoiceFour == "yes":
#                     totalDateMoney = totalDateMoney - starLightLanes
#                     print("You went bowling and had a good time. You end the date with a total of " + str(totalDateMoney) + " dollars.")
#                 else:
#                     print("Ok you decided to go home.")
#         else:
#             totalDateMoney = totalDateMoney - (moonLightBoat * 2)
#             print("\nYou decided to not go to a movie.")
#             print("You decide to go to the moonlight boat trip that is 35 dollars a person. You have a good time and have "
#                   + str(totalDateMoney) + " dollars remaining.")
#
#
# else:
#     print("\nThe latest large-screen film presentation of the hot blockbuster superhero movie is playing at 7 p.m.\n")
#     totalDateMoney = totalDateMoney - superHeroMovie
#     ChoiceAlt = input("You enjoyed the movie. Where would you like to go out to eat?\nYou only have " + str(totalDateMoney) +
#                       " dollars remaining.\n"
#                       "\n--Ten Guys does burgers of varying sizes with fries and a drink for about $12 a person.\n"
#                       "--Fancy-Dogs will get you a custom gourmet hot dog and tornado fries for $15 a person.\n"
#                       "\nType hotdog or burger :  ")
#     if ChoiceAlt == "hotdog":
#         totalDateMoney = totalDateMoney - (hotDog * 2)
#         ChoiceAlt2 = input("\nYou ate a hot dog and fries with your date and had a good time.\nYou have " + str(totalDateMoney) +
#               " dollars remaining.\nStar Light Lanes has announced a happy hour Cosmic Bowl-a-Rama for $30, going from 9 p.m. to midnight.\n"
#               "\nDo you go to the bowling lane or go home? Type bowl or home : ")
#         if ChoiceAlt2 == "bowl":
#             totalDateMoney = totalDateMoney - starLightLanes
#             print("\nYou went bowling and had a great time. You finish the date off and have a remaining balance of " + str(totalDateMoney) +
#                   " dollars. ")
#
#         else:
#             print("You end the date went home and had a remaining balance of 55 dollars. ")
#
#
#
#     else:
#         totalDateMoney = totalDateMoney - (tenGuysBurgers * 2)
#         print("You ate a burger, fires, and drink with your date. You have " + str(totalDateMoney) +
#               " dollars remaining after your date. You decide you want to save your money and you cut the date short and go home.")

firstDistance = 1
optionTwo = 4

def my_function():
    print("-----------------------------------------------------------------------------------")
# function for line of instructions

def my_instructions():
    seconddistance = 1
    while seconddistance != 4:
        seconddistance += 1
        print("\nKeep driving. You are at exit " + str(seconddistance - 1) + ".")
        if seconddistance == 4:
            print("\nYou are approaching exit 4.")
            optionTwo = int(input("\nDo you take exit 4 or exit 5? Type '5' or '4': "))
            if optionTwo == 5:
                print("\nYou have gone to far!")
                while optionTwo != 4:
                    print("\nTurn back around...")
                    optionTwo = int(input("\nDo you take exit 4 or exit 5? Type '5' or '4': "))
                    if optionTwo == 4:
                        print("\nYou have finally arrived home!")
                        break
            elif optionTwo == 4:
                print("\nYou have finally arrived home!")
# function for direction options


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

#





