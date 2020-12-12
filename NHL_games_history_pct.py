#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
  
print("Content-type: text/html\n\r\n")
import mysql.connector
import cgi, cgitb
import re

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
sort_field = form.getvalue('sort_field')
#
# set up the mysql database table connection where each simulation run result is stored
#
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
if sort_field == "Fposition" or sort_field == "dt" or sort_field == "points":
	sel = "SELECT * from NHL_Season where points > 118 or points < 40 order by "+sort_field
else:
	sel = "SELECT * from NHL_Season where points > 118 or points < 40 order by "+sort_field+" desc"
mycursor.execute(sel)
myresult = mycursor.fetchall()
header = "<b><center><p style='color:blue;'> 2020-21 NHL Season Simulator v1.0 - Final Standings @Copyright Wilky Consultants Inc.</p></b><table border='1' class='dataframe'>\n"
print(header)
header = "<thead><tr style='text-align: center;'><th>Season#</th><th><a href=NHL_games_history_pct.py?sort_field=dt>Date/Time</a></th><th><a href=NHL_games_history_pct.py?sort_field=team>Team</a></th><th><a href=NHL_games_history_pct.py?sort_field=wins>Wins</th><th><a href=NHL_games_history_pct.py?sort_field=loses>Loses</a></a></th><th><a href=NHL_games_history_pct.py?sort_field=otl>OTL</a></th><th><a href=NHL_games_history_pct.py?sort_field=conference>Conference</a></th><th><a href=NHL_games_history_pct.py?sort_field=points>Points</a></th><th><a href=NHL_games_history_pct.py?sort_field=pct_points>%Points</a></th><th><a href=NHL_games_history_pct.py?sort_field=GF>GF</a></th><th><a href=NHL_games_history_pct.py?sort_field=GA>GA</a></th><th><a href=NHL_games_history_pct.py?sort_field=games>Games</a></th><th><a href=NHL_games_history_pct.py?sort_field=Fposition>Finish</a></th></tr></thead><tbody>\n"
print(header)

for res in myresult:
    mycursor2 = mydb.cursor()
    sel2 = "SELECT id from NHL_counter where dt='"+res[1]+"'"
    mycursor2.execute(sel2)
    myresult2 = mycursor2.fetchall()
    for res2 in myresult2:
        counter = res2[0]
    html = "<tr><td align=center>"+str(counter)+"</td><td><a href=NHL_reshow.py?dt_run="+res[1]+">"+res[1]+"</a></td><td>"+res[2]+"</td><td align=center>"+str(res[3])+"</td><td align=center>"+str(res[4])+"</td><td align=center>"+str(res[5])+"</td><td>"+res[6]+"</td><td align=center>"+str(res[7])+"</td><td align=center>"+str(res[8])+"</td><td align=center>"+str(res[9])+"</td><td align=center>"+str(res[10])+"</td><td align=center>"+str(res[11])+"</td><td align=center>"+str(res[12])+"</td></tr>"
    print(html)
mydb.close()
