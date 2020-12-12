#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
  
print("Content-type: text/html\n\r\n")
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
sql = "select  distinct team from nhl_season order by team;" 
mycursor.execute(sql)
myresult_teams = mycursor.fetchall()
teamnames = []
for row in myresult_teams:
    teamnames.append(row[0])
i=0
teams = []
sql = "select count(Fposition) from nhl_season where team='Toronto Maple Leafs';"
mycursor.execute(sql)
myresult_count = mycursor.fetchall()
for res_count in myresult_count:
    total_count=res_count[0]
print("<pre><center><h1>Cross reference of distribution of finishing positions by count</pre></h1>")
print("<pre><center><h2>Total Simulations: "+str(total_count)+"</pre></h2>")

print("<table border=1 style='border:1px solid black;margin-left:auto;margin-right:auto;'>")
html=""
chk_ctr=0
while chk_ctr < 31:
      chk_ctr=chk_ctr+1
      html=html+"<td align=center><b>"+str(chk_ctr)+"</td>"
print("<tr><td><b>Team/Position</td>",html,"</tr>")
for teamname in teamnames:
  html=""
  sql = "select  Fposition,count(Fposition) from nhl_season where team='"+teamname+"' group by Fposition order by Fposition;" 
  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  sql = "select count(Fposition) from nhl_season where team='"+teamname+"';"
  mycursor.execute(sql)
  myresult_count = mycursor.fetchall()
  for res_count in myresult_count:
      total_count=res_count[0]
  chk_ctr=1
  for res in myresult:
      total_count=res_count[0]
      calc_pct=res[1]/total_count*100
      if calc_pct > 10:
         bgcolor="#65c368"
      elif calc_pct < 10 and calc_pct > 6:
         bgcolor="#82df83"
      elif calc_pct < 6 and calc_pct > 3:
         bgcolor="#90ee90"
      elif calc_pct < 3 and calc_pct > .5:
         bgcolor="#BDFCC9"
      else:
         bgcolor="#C1FFC1"
      #print("calc_pct=",calc_pct," - bgcolor=",bgcolor)
      while chk_ctr != res[0]:
            chk_ctr=chk_ctr+1
            html=html+"<td align=center bgcolor=#E0EEE0>-</td>"
      html=html+"<td align=center bgcolor="+bgcolor+">"+str(res[1])+"</td>"
      chk_ctr=chk_ctr+1
  if chk_ctr != 32:
     while chk_ctr < 32:
         chk_ctr=chk_ctr+1
         #print(teamnames[teamname],res[0],res[1], chk_ctr)
         html=html+"<td align=center bgcolor=#E0EEE0>-</td>"
  print("<tr><td nowrap>",teamname,"</td>",html,"</tr>")
mydb.close()
