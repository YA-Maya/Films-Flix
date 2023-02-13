import read1
import insertData1
import update1
import delete1

# create a function
def menuOptions():
    options = 0  # flag variable

    while options not in ["1", "2", "3", "4", "5"]:
        print(
            "Films Menu Options\nEnter \n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Exit."
        )
        # re-assign options variable with a new value
        options = input("\nEnter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5"]:
            print(f"{options} is not a valid choice")
    return options


mainProgram = True  # flag variable
while mainProgram == True:
    mainMenu = menuOptions()
    if mainMenu == "1":
        read1.readFilms()
    elif mainMenu == "2":
        insertData1.addFilms()
    elif mainMenu == "3":
        update1.updateFilms()
    elif mainMenu == "4":
        delete1.deleteFilm()
    else:  # reassign mainProgram to False
        mainProgram = False
input("press ENter to Exit")
