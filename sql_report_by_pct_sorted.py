#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
  
print("Content-type: text/html\n\r\n")
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
sql = "select  distinct team from nhl_season order by team;" 
mycursor.execute(sql)
myresult_teams = mycursor.fetchall()
# 2d dictionary to store team name and 31 values of positions
rows, cols = (31, 33)
#teamnames=[[0]*cols]*rows
teamnames = [[0 for i in range(cols)] for j in range(rows)]
ctr=0
for row in myresult_teams:
    #print(row)
    #print("Adding array element [",ctr,"][",0,"] as "+row[0])
    teamnames[ctr][0]=row[0]
    #print("SET: ",teamnames[ctr][0])
    for ctr2 in range(1,33):
       teamnames[ctr][ctr2]=0.00
       #print("SET : [",ctr,"][",ctr2,"] to ",teamnames[ctr][ctr2])
    ctr=ctr+1
#print(teamnames)
#print("0,0",teamnames[0][0])
i=0
sql = "select count(Fposition) from nhl_season where team='Toronto Maple Leafs';"
mycursor.execute(sql)
myresult_count = mycursor.fetchall()
for res_count in myresult_count:
    total_count=res_count[0]
print("<pre><center><h1>Cross reference of distribution of finishing positions by percentage</pre></h1>")
print("<pre><center><h2>Total Simulations: "+str(total_count)+"</pre></h2>")
#teams = []
##print("<table border=1 style='border:1px solid black;margin-left:auto;margin-right:auto;'>")
html=""
ctr_x=0
ctr_y=0
chk_ctr=0
while chk_ctr < 31:
      chk_ctr=chk_ctr+1
      html=html+"<td align=center><b>"+str(chk_ctr)+"</td>"
##print("<tr><td><b>Team/Position</td>",html,"</tr>")
for teamname in teamnames:
  #print(teamnames[ctr_x][0])
  html=""
  if ctr_x > 30:
     break
  tm=teamnames[ctr_x][0]
  sql = "select  Fposition,count(Fposition) from nhl_season where team='"+tm+"' group by Fposition order by Fposition;" 
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  sql = "select count(Fposition) from nhl_season where team='"+tm+"';" 
  mycursor.execute(sql)
  myresult_count = mycursor.fetchall()
  for res_count in myresult_count:
      total_count=res_count[0]
  chk_ctr=1
  for res in myresult:
      calc_pct=res[1]/total_count*100
      calc_pct_print_conv=round(res[1]/total_count*100,2)
      teamnames[ctr_x][ctr_y+1]=calc_pct_print_conv
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
#
# will loop in here creating empty cells because this position was never created for this team
#
      while chk_ctr != res[0]:
            teamnames[ctr_x][ctr_y+1]=0.0
            chk_ctr=chk_ctr+1
            ctr_y=ctr_y+1
            ##html=html+"<td align=center bgcolor=#E0EEE0>-</td>"
#
      calc_pct_print=str(round(res[1]/total_count*100,2))
      if calc_pct == "0.0":
         calc_pct=""
      ##html=html+"<td align=center bgcolor="+bgcolor+">"+calc_pct_print+"</td>"
      teamnames[ctr_x][ctr_y+1]=calc_pct_print_conv
      chk_ctr=chk_ctr+1
      ctr_y=ctr_y+1
  if chk_ctr != 32:
     while chk_ctr < 32:
         chk_ctr=chk_ctr+1
         ctr_y=ctr_y+1
         ##html=html+"<td align=center bgcolor=#E0EEE0>-</td>"
  ctr_y=0
  ##print("<tr><td nowrap>",teamnames[ctr_x][0],"</td>",html,"</tr>")
  ctr_x=ctr_x+1
#print("</table>")
#
teamnames = sorted(teamnames, key=lambda x: (x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16]),reverse=True)
#teamnames = sorted(teamnames, key=lambda x: (x[1],x[2], reverse=True))
#sorted_teams = sorted(teams, key=lambda x: (x[2],x[0]))
##teamnames.sort(key=lambda x: x[1], reverse=True)
#
#print(teamnames)
mydb.close()
print("<table border=1 style='border:1px solid black;margin-left:auto;margin-right:auto;'>")
chk_ctr=0
while chk_ctr < 31:
      chk_ctr=chk_ctr+1
      html=html+"<td align=center><b>"+str(chk_ctr)+"</td>"
print("<tr><td><b>Team/Position</td>",html,"</tr>")
for rows in range(0,31):
    print("<tr><td nowrap>",teamnames[rows][0],"</td>")
    for cols in range(1,32):
        calc_pct=teamnames[rows][cols]
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

        if teamnames[rows][cols] == 0.0:
            print("<td align=center bgcolor=",bgcolor,">_</td>")
        else:
            print("<td align=center bgcolor=",bgcolor,">",teamnames[rows][cols],"</td>")
print("</table>")
