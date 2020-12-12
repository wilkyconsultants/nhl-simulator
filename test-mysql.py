#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS NHL")
mydb.close()
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE IF NOT EXISTS NHL_Season (id INT AUTO_INCREMENT PRIMARY KEY, dt VARCHAR(255), team VARCHAR(255), wins DECIMAL(4,0), loses DECIMAL(4,0), otl DECIMAL(4,0), conference VARCHAR(255), points DECIMAL(4,0), pct_points DECIMAL(4,3), gf DECIMAL(4,0), ga DECIMAL(4,0), games DECIMAL(4,0));")
mycursor.execute("CREATE TABLE IF NOT EXISTS NHL_Season (id INT AUTO_INCREMENT PRIMARY KEY, dt VARCHAR(255), team VARCHAR(255), wins DECIMAL(4,0), loses DECIMAL(4,0), otl DECIMAL(4,0), conference VARCHAR(255), points DECIMAL(4,0), pct_points DECIMAL(4,3), gf DECIMAL(4,0), ga DECIMAL(4,0), games DECIMAL(4,0));")
dt = "2020-11-26_122220"
team = "Toronto Maple Leafs"
wins = 50
loses = 20
otl = 12
conference = "Eastern"
points = 112
pct_points = 0.701
gf = 300
ga = 200
games = 82

##sql_insert_query = """ INSERT INTO NHL_Season 
##                        (id, dt, team, wins, loses, otl, conference, points, pct_points, gf, ga, games) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

##insert_tuple_1 = (None, dt, team, wins, loses, otl, conference, points, pct_points, gf, ga, games)
#insert_tuple_1 = (1, dt, team, wins, loses, otl, conference, points, pct_points, gf, ga, games)
##mycursor = mydb.cursor()
##mycursor.execute(sql_insert_query, insert_tuple_1)
##mydb.commit()
sql = "SELECT count(DISTINCT dt) from NHL_Season"
mycursor = mydb.cursor()
sel = mycursor.execute(sql)
myresult = mycursor.fetchall()
for res in myresult:
    print(res[0])

#mycursor = mydb.cursor()
#sql = "DROP TABLE if EXISTS NHL_Season"
#mycursor.execute(sql)
#sql = "DROP DATABASE if exists NHL"
#mycursor.execute(sql)
mydb.close()
