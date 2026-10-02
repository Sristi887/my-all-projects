import sqlite3;
connection = sqlite3.connect("database.db");
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor();

cursor.execute('''CREATE TABLE IF NOT EXISTS student( 
Roll_no INTEGER PRIMARY KEY,
name TEXT NOT NULL)''');

cursor.execute('''CREATE TABLE IF NOT EXISTS marks( 
Roll_no INTEGER ,
subject TEXT NOT  NULL,
marks INTEGER NOT NULL,
PRIMARY KEY(Roll_no, subject),
FOREIGN KEY(Roll_no) REFERENCES student(Roll_no))''');

connection.commit();
connection.close();