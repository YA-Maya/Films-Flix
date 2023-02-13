from sqliteConnect1 import *

cursor.execute(
    """ 

CREATE TABLE "Film" (
	"FilmID"	INTEGER NOT NULL UNIQUE,
	"YearReleased"	INTEGER,
	"Rating"	TEXT,
	"Duration"	INTEGER,
    "Genre"	TEXT,
	PRIMARY KEY("FilmID" AUTOINCREMENT)
)"""
)
# ...............................
