from sqliteConnect1 import *
import read1
import time


def deleteFilm():
    # filmID of the record to be updated
    idField = input("Enter the filmID of the movie to be deleted : ")

    cursor.execute(f"DELETE FROM film WHERE FilmID={idField}")
    conn.commit()

    print(f"Record {idField} deleted")
    time.sleep(3)
    read1.readFilms()  # invoke readSongs subroutine from the read app


# deleteFilm()