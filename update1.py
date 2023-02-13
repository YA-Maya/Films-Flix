from sqliteConnect1 import *
import read1
import time


def updateFilms():
    # filmID of the record to be updated
    idField = input("Enter the filmID of the film to be updated : ")
    # enter the name of the field to be updated
    fieldTile = input(
        "Which field would you like to update(Title, Rating, Genre?): "
    ).title()
    # Enter the new field value
    newfieldValue = input(f"Enter the new field value for {fieldTile} ")
    print(f"The new field value enteed is {newfieldValue}")

    # add single quotes around the field value entered by the user
    # name =  Anna . now name = " ' " +  Anna + "  ' ""

    newfieldValue = "'" + newfieldValue + "'"
    print(f"The new field value enteed is {newfieldValue}")

    # update the movie in films table
    "UPDATE films SET Title/Rating/Genre = newfieldValue(light off/4/horror) "
    cursor.execute(
        f"UPDATE films SET {fieldTile} = {newfieldValue} WHERE filmID = {idField}"
    )
    conn.commit()

    print(f"Record {idField} updated")
    time.sleep(3)
    read1.readFilms()  # invoke readFilms subroutine from the read app


# updateFilms()  # call/invoke update songs subroutine
