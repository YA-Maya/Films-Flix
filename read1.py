from sqliteConnect1 import *


def readFilms():
    cursor.execute("SELECT * FROM films")  # select all records from films table

    row = cursor.fetchall()  # fetch all the films that was selected in the table

    for (
        record
    ) in (
        row
    ):  # iterate through all the records held in the row variable and print one at a time
        print(record)


# readFilms()  # invoke/call read films subroutine