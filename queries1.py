from os import curdir
from sqliteConnect1 import *

cursor.exectute("SELECT FROM tblfilms WHERE genre = COMEDY/Action ")

cursor.exectute("SELECT FROM tblfilms WHERE yearReleased = 2016 ")

cursor.exectute("SELECT FROM tblfilms WHERE rating = PG ")