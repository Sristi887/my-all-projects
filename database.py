import sqlite3;
connection = sqlite3.connect("database.db");
cursor = connection.cursor();

cursor.execute('''CREATE TABLE student( 
Roll no INTEGER PRIMARY KEY,
name TEXT)''');

connection.commit();
connection.close();