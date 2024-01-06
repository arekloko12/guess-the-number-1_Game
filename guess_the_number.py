# Author of the game is: arekloko
# Date of creation: 04.01.2024
# Last update: 06.01.2024

import random


print("Welcome to mini game")

# Important functions

def app_close():
    exit()

def rules():
    global trying
    trying = 10

    print("------------------------------------")
    print("Rules:\nThe computer will generate a random number depending on the chosen level of the game.\nYou have to guess what number it is. You have three attempts.\nIf you answer incorrectly, a hint about the winning number will be displayed.\nGood Luck!\n\nLevels:\nEasy: 1-10\nMedium: 1-50\nHard: 1-100\nVery hard: 1-500\nImposible: 1-1000\n ")
    print("------------------------")
    for i in range(10):
        back = input("1 - Back to menu\n2 - Close the app\n")
        trying -= 1

        if back.isdigit():
            back = int(back)
        elif trying > 0:
            print("Invalid input! Try again.")
            continue
        elif trying == 0:
            print("------------------------------------")
            print("Too many attempts")
            print("\nClosing application...")
            print("------------------------------------")
            app_close()

        if back == 1:
            start_game_menu()
        elif back == 2:
            print("\nClosing application...\n")
            app_close()
        elif trying > 0:
            print("------------------------------------")
            print("Wrong command! Try again.")
            print("------------------------------------")
        elif trying == 0:
            print("------------------------------------")
            print("Too many attempts")
            print("\nClosing application...")
            print("------------------------------------")
            app_close()

# Game

def start_game():
    print("----------------------------------------")
    global level_selection
    trying = 10
    for i in range(10):
        level_selection = input("Choose a level:\n1 - easy,\n2 - medium,\n3 - hard,\n4 - very hard,\n5 - imposible\n")
        trying -= 1

        if level_selection.isdigit():
            level_selection = int(level_selection)
        elif trying > 0:
            print("Invalid input! Try again.")
            continue
        elif trying == 0:
            print("------------------------------------")
            print("Too many attempts")
            print("\nClosing application...")
            print("------------------------------------")
            app_close()

        if level_selection == 1:
            level_1()
        elif level_selection == 2:
            level_2()
        elif level_selection == 3:
            level_3()
        elif level_selection == 4:
            level_4()
        elif level_selection == 5:
            level_5()
        elif trying > 0:
            print("------------------------------------")
            print("Wrong command! Try again.")
            print("------------------------------------")
        elif trying == 0:
            print("------------------------------------")
            print("Too many attempts")
            print("\nClosing application...")
            print("------------------------------------")
            app_close()

def level_1():
    global rand_number
    global attempts
    global trying
    attempts = 3
    rand_number = random.randint(1, 10)
    trying = 10

    
    #checking number; user number == number drawn
    for i in range(20):
        trying = 10

        print("----------------------------")
        print("You have "+str(attempts)+" attempts")
        print("----------------------------")

        for i in range(20):
            user_number = input("Choose a number ")
            print("__________________________________________")

            if user_number.isdigit():
                user_number = int(user_number)
                attempts -=1
                break
            elif trying > 0:
                print("Invalid input! Try again.")
                trying -= 1
                continue
            elif trying == 0:
                print("------------------------------------")
                print("Too many attempts")
                print("\nClosing application...")
                print("------------------------------------")
                app_close()
            
        for i in range(20):

            if user_number == rand_number:
                print("_________________________________________________")
                print("Congratulations! You guessed the right number.")
                print("_________________________________________________")
                app_close()
            elif user_number != rand_number and attempts > 0:
                print("Sorry, that's not the number")
                print("----------------------------")
                print("You have "+str(attempts)+" attempts")
                print("----------------------------")
                for i in range(10):
                    hint()
                    user_number = input("Try again ")
                    print("----------------")
                    if user_number.isdigit():
                        user_number = int(user_number)
                        attempts -= 1
                        break
                    elif trying > 0:
                        print("Invalid input! Try again. ")
                        trying -= 1
                        continue
                    elif trying <= 0:
                        print("------------------------------------")
                        print("Too many attempts")
                        print("\nClosing application...")
                        print("------------------------------------")
                        app_close()

            elif attempts <= 0 and user_number != rand_number :
                print("_________________________________________________")
                print("Game Over! The correct answer was ",rand_number)
                print("_________________________________________________")
                app_close()

def level_2():
    global rand_number
    global attempts
    global trying
    attempts = 3
    rand_number = random.randint(1, 50)
    trying = 10

    
    #checking number; user number == number drawn
    for i in range(20):
        trying = 10

        print("----------------------------")
        print("You have "+str(attempts)+" attempts")
        print("----------------------------")

        for i in range(20):
            user_number = input("Choose a number ")
            print("__________________________________________")

            if user_number.isdigit():
                user_number = int(user_number)
                attempts -=1
                break
            elif trying > 0:
                print("Invalid input! Try again.")
                trying -= 1
                continue
            elif trying == 0:
                print("------------------------------------")
                print("Too many attempts")
                print("\nClosing application...")
                print("------------------------------------")
                app_close()
            
        for i in range(20):

            if user_number == rand_number:
                print("_________________________________________________")
                print("Congratulations! You guessed the right number.")
                print("_________________________________________________")
                app_close()
            elif user_number != rand_number and attempts > 0:
                print("Sorry, that's not the number")
                print("----------------------------")
                print("You have "+str(attempts)+" attempts")
                print("----------------------------")
                for i in range(10):
                    hint()
                    user_number = input("Try again ")
                    print("----------------")
                    if user_number.isdigit():
                        user_number = int(user_number)
                        attempts -= 1
                        break
                    elif trying > 0:
                        print("Invalid input! Try again. ")
                        trying -= 1
                        continue
                    elif trying <= 0:
                        print("------------------------------------")
                        print("Too many attempts")
                        print("\nClosing application...")
                        print("------------------------------------")
                        app_close()

            elif attempts <= 0 and user_number != rand_number :
                print("_________________________________________________")
                print("Game Over! The correct answer was ",rand_number)
                print("_________________________________________________")
                app_close()

def level_3():
    global rand_number
    global attempts
    global trying
    attempts = 3
    rand_number = random.randint(1, 100)
    trying = 10

    #checking number; user number == number drawn
    for i in range(20):
        trying = 10

        print("----------------------------")
        print("You have "+str(attempts)+" attempts")
        print("----------------------------")

        for i in range(20):
            user_number = input("Choose a number ")
            print("__________________________________________")

            if user_number.isdigit():
                user_number = int(user_number)
                attempts -=1
                break
            elif trying > 0:
                print("Invalid input! Try again.")
                trying -= 1
                continue
            elif trying == 0:
                print("------------------------------------")
                print("Too many attempts")
                print("\nClosing application...")
                print("------------------------------------")
                app_close()
            
        for i in range(20):

            if user_number == rand_number:
                print("_________________________________________________")
                print("Congratulations! You guessed the right number.")
                print("_________________________________________________")
                app_close()
            elif user_number != rand_number and attempts > 0:
                print("Sorry, that's not the number")
                print("----------------------------")
                print("You have "+str(attempts)+" attempts")
                print("----------------------------")
                for i in range(10):
                    hint()
                    user_number = input("Try again ")
                    print("----------------")
                    if user_number.isdigit():
                        user_number = int(user_number)
                        attempts -= 1
                        break
                    elif trying > 0:
                        print("Invalid input! Try again. ")
                        trying -= 1
                        continue
                    elif trying <= 0:
                        print("------------------------------------")
                        print("Too many attempts")
                        print("\nClosing application...")
                        print("------------------------------------")
                        app_close()

            elif attempts <= 0 and user_number != rand_number :
                print("_________________________________________________")
                print("Game Over! The correct answer was ",rand_number)
                print("_________________________________________________")
                app_close()
def level_4():
    global rand_number
    global attempts
    global trying
    attempts = 3
    rand_number = random.randint(1, 500)
    trying = 10

    
    #checking number; user number == number drawn
    for i in range(20):
        trying = 10

        print("----------------------------")
        print("You have "+str(attempts)+" attempts")
        print("----------------------------")

        for i in range(20):
            user_number = input("Choose a number ")
            print("__________________________________________")

            if user_number.isdigit():
                user_number = int(user_number)
                attempts -=1
                break
            elif trying > 0:
                print("Invalid input! Try again.")
                trying -= 1
                continue
            elif trying == 0:
                print("------------------------------------")
                print("Too many attempts")
                print("\nClosing application...")
                print("------------------------------------")
                app_close()
            
        for i in range(20):

            if user_number == rand_number:
                print("_________________________________________________")
                print("Congratulations! You guessed the right number.")
                print("_________________________________________________")
                app_close()
            elif user_number != rand_number and attempts > 0:
                print("Sorry, that's not the number")
                print("----------------------------")
                print("You have "+str(attempts)+" attempts")
                print("----------------------------")
                for i in range(10):
                    hint()
                    user_number = input("Try again ")
                    print("----------------")
                    if user_number.isdigit():
                        user_number = int(user_number)
                        attempts -= 1
                        break
                    elif trying > 0:
                        print("Invalid input! Try again. ")
                        trying -= 1
                        continue
                    elif trying <= 0:
                        print("------------------------------------")
                        print("Too many attempts")
                        print("\nClosing application...")
                        print("------------------------------------")
                        app_close()

            elif attempts <= 0 and user_number != rand_number :
                print("_________________________________________________")
                print("Game Over! The correct answer was ",rand_number)
                print("_________________________________________________")
                app_close()

def level_5():
    global rand_number
    global attempts
    global trying
    attempts = 3
    rand_number = random.randint(1, 1000)
    trying = 10

    
    #checking number; user number == number drawn
    for i in range(20):
        trying = 10

        print("----------------------------")
        print("You have "+str(attempts)+" attempts")
        print("----------------------------")

        for i in range(20):
            user_number = input("Choose a number ")
            print("__________________________________________")

            if user_number.isdigit():
                user_number = int(user_number)
                attempts -=1
                break
            elif trying > 0:
                print("Invalid input! Try again.")
                trying -= 1
                continue
            elif trying == 0:
                print("------------------------------------")
                print("Too many attempts")
                print("\nClosing application...")
                print("------------------------------------")
                app_close()
            
        for i in range(20):

            if user_number == rand_number:
                print("_________________________________________________")
                print("Congratulations! You guessed the right number.")
                print("_________________________________________________")
                app_close()
            elif user_number != rand_number and attempts > 0:
                print("Sorry, that's not the number")
                print("----------------------------")
                print("You have "+str(attempts)+" attempts")
                print("----------------------------")
                for i in range(10):
                    hint()
                    user_number = input("Try again ")
                    print("----------------")
                    if user_number.isdigit():
                        user_number = int(user_number)
                        attempts -= 1
                        break
                    elif trying > 0:
                        print("Invalid input! Try again. ")
                        trying -= 1
                        continue
                    elif trying <= 0:
                        print("------------------------------------")
                        print("Too many attempts")
                        print("\nClosing application...")
                        print("------------------------------------")
                        app_close()

            elif attempts <= 0 and user_number != rand_number :
                print("_________________________________________________")
                print("Game Over! The correct answer was ",rand_number)
                print("_________________________________________________")
                app_close()


def hint():
    checking_number_1 = 1
    checking_number_2 = 0
    number_table = []

    if level_selection == 1:
        i = 10
    elif level_selection == 2:
        i = 50
    elif level_selection == 3:
        i = 100
    elif level_selection == 4:
        i = 500
    elif level_selection == 5:
        i = 1000

    if attempts > 1:
        for i in range(i):
            if rand_number % checking_number_1 == 0 and rand_number != checking_number_1:
                number_table.append(checking_number_1)
                checking_number_1 += 1
                continue
            else:
                checking_number_1 += 1
                continue

        print("Number is divisible by ",number_table)
    elif attempts == 1:
        for i in range(i):
            if rand_number <= checking_number_2:
                print("Number is less than or equal to ",checking_number_2)
                break
            else:
                checking_number_2 += 3
                continue
        
# Game menu
def start_game_menu():
    trying = 10
    print("-----------------------------------------")
    for i in range(10):
        start = input("Choose option: 1 - Start game, 2 - Rules ")
        trying -= 1
        if start.isdigit():
            start = int(start)
        elif trying > 0:
            print("Invalid input! Try again.")
            continue
        elif trying == 0:
            print("------------------------------------")
            print("Too many attempts")
            print("\nClosing application...")
            print("------------------------------------")
            app_close()

        if start == 1:
            start_game()
        elif start == 2:
            rules()
        elif trying > 0:
            print("------------------------------------")
            print("Wrong command! Try again.")
            print("------------------------------------")
        elif trying == 0:
            print("------------------------------------")
            print("Too many attempts")
            print("\nClosing application...")
            print("------------------------------------")
            app_close()

start_game_menu()