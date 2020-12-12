#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
  
print("Content-type: text/html\n\r\n")
import mysql.connector
import cgi, cgitb
import re

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
t = form.getvalue('t')
sort_field = form.getvalue('sort_field')
if t == "St.":
        x = "St."
        t = "St. Louis"
else:
        x = t[0:len(t)]
png = "<center><img src='/"+x+".png' width=180 height=150><br>"
print(png)
#
# set up the mysql database table connection where each simulation run result is stored
#
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
if sort_field != "Fposition":
   sel = "SELECT * from NHL_Season where team LIKE '%"+x+"%'"
else:
   sel = "SELECT * from NHL_Season where team LIKE '%"+x+"%' order by Fposition,Points desc"
mycursor.execute(sel)
myresult = mycursor.fetchall()
header = "<b><center><p style='color:blue;'> 2020-21 NHL Season Simulator v1.0 - Final Standings @Copyright Wilky Consultants Inc.</p></b><table border='1' class='dataframe'>\n"
print(header)
header = "<thead><tr style='text-align: center;'><th>Simulation#</th><th>Date/Time</th><th>Team</th><th>Wins</th><th>Loses</th><th>OTL</th><th>Conference</th><th>Points</th><th>%Points</th><th>GF</th><th>GA</th><th>Games</th><th>Finish</th></tr></thead><tbody>\n"
print(header)

for res in myresult:
    mycursor2 = mydb.cursor()
    sel2 = "SELECT id from NHL_counter where dt='"+res[1]+"'"
    mycursor2.execute(sel2)
    myresult2 = mycursor2.fetchall()
    for res2 in myresult2:
        counter = res2[0]
    html = "<tr><td align=center>"+str(counter)+"</td><td><a href=NHL_games.py?dt_run="+res[1]+"&t="+t+">"+res[1]+"</a></td><td>"+res[2]+"</td><td align=center>"+str(res[3])+"</td><td align=center>"+str(res[4])+"</td><td align=center>"+str(res[5])+"</td><td>"+res[6]+"</td><td align=center>"+str(res[7])+"</td><td align=center>"+str(res[8])+"</td><td align=center>"+str(res[9])+"</td><td align=center>"+str(res[10])+"</td><td align=center>"+str(res[11])+"</td><td align=center>"+str(res[12])+"</td></tr>"
    print(html)
mydb.close()
