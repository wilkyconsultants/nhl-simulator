#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

print("Content-type: text/html\n\r\n")
import mysql.connector
import datetime
import cgi, cgitb
#
# Create instance of FieldStorage
form = cgi.FieldStorage()
#
# Get data from fields
dt_run = form.getvalue('dt_run')
#
# set up the mysql database table connection where each simulation run result is stored
#
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
sel = "SELECT * from NHL_Season where dt='"+dt_run+"' order by pct_points desc"
mycursor.execute(sel)
myresult = mycursor.fetchall()
header = "<b><center><p style='color:blue;'> 2020-21 NHL Season Simulator v1.0 - Final Standings(Reshow) @Copyright Wilky Consultants Inc.</p></b><table border='1' class='dataframe'>\n"
print(header)
header = "<center><p style='color:green;'>Reshow Simulation: "+dt_run
print(header)
header = "<thead><tr style='text-align: center;'><th>Team</th><th>Wins</th><th>Loses</th><th>OTL</th><th>Conference</th><th>Points</th><th>%Points</th><th>GF</th><th>GA</th><th>Games</th></tr></thead><tbody>\n"
print(header)

for res in myresult:
    html = "<tr><td>"+res[2]+"</td><td align=center>"+str(res[3])+"</td><td align=center>"+str(res[4])+"</td><td align=center>"+str(res[5])+"</td><td>"+res[6]+"</td><td align=center>"+str(res[7])+"</td><td align=center>"+str(res[8])+"</td><td align=center>"+str(res[9])+"</td><td align=center>"+str(res[10])+"</td><td align=center>"+str(res[11])+"</td></tr>"
    print(html)

