#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
sql = "select  distinct team from nhl_season order by team;" 
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("teamnames = [")
for res in myresult:
   print("   '"+res[0]+"',")
print(" ]")
