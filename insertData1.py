from sqliteConnect1 import *
import time

# create a subroutine to add movie to the film table in the database
def addFilms():
    # create an empty list
    films = []

    title = input("Enter film title: ")
    yearReleased = input("Enter year released: ")
    genre = input("Enter films genre: ")
    Rating = input("Enter films rating: ")

    # append data captured from the user into the films list
    " songs.SongID is set to auto increment and would be added automatically"

    films.append(title)
    films.append(yearReleased)
    films.append(genre)
    films.append(Rating)

    # insert data from the list into films table

    cursor.execute("INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?)", films)
    conn.commit()  # commit/write changes permanently to the database
    print(f"{title} added to tblFilms")

    time.sleep(3)

    cursor.execute("SELECT * FROM tblFilms")  # select all records from film table

    row = cursor.fetchall()  # fetch all the films that was selected in the table

    for (
        record
    ) in (
        row
    ):  # iterate through all the records held in the row variable and print one at a time
        print(record)


# addfilms()  # call/invoke the subroutine
