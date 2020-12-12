#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

print("Content-type: text/html\n\r\n")
import random
import pandas as pd
import re
import time
import mysql.connector
#import os
#import sys
#import cgi
import datetime
x = datetime.datetime.now()
dt = x.strftime("%Y-%m-%d %H:%M:%S")
dt_run = x.strftime("%Y-%m-%d_%H%M%S%f")
print("<form action='/cgi-bin/NHL_SIMULATION/NHL.py'>")
# variables
#cmd = "ls"
#sys.stdout.flush()
#a = os.system(cmd)
#print(str(a))
game_loop = 1  # 1=82 games, 2=164 games  , etc
teamA = 0
teamH = 0
scoreA = 0
scoreH = 0
team = 0
points = 0
teamAName = 'TeamA'
teamHName = 'TeamH'
spacer = ''
simGames = False
gameResult = [0, 0, 0]
#
# set up the mysql database table connection to store each simulation run result
#
mydb = mysql.connector.connect(host="localhost", user="root")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS NHL")
mydb.close()
mydb = mysql.connector.connect(host="localhost", user="root", database="NHL")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS NHL_Season (id INT AUTO_INCREMENT PRIMARY KEY, dt VARCHAR(255), team VARCHAR(255), wins DECIMAL(4,0), loses DECIMAL(4,0), otl DECIMAL(4,0), conference VARCHAR(255), points DECIMAL(4,0), pct_points DECIMAL(4,3), gf DECIMAL(4,0), ga DECIMAL(4,0), games DECIMAL(4,0), Fposition DECIMAL(4,0));")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS NHL_counter (id INT AUTO_INCREMENT PRIMARY KEY, dt VARCHAR(255));")
#
# Count the number of similations we have ran
#
mycursor = mydb.cursor()
#sql = "SELECT count(DISTINCT id) from NHL_counter"
#sql = "SELECT count(DISTINCT dt) from NHL_Season"
sql = "select count(Fposition) from nhl_season where team='Toronto Maple Leafs';"
sel = mycursor.execute(sql)
myresult = mycursor.fetchall()
for res in myresult:
    simulation_ctr = res[0]+1

#xlsx = pd.ExcelFile("/Users/robwilk/PycharmProjects/pythonProjectWEB/NHL_2018-19_Schedule.xlsx")
xlsx = pd.ExcelFile("/Library/WebServer/CGI-Executables/NHL_SIMULATION/NHL_2018-19_Schedule.xlsx")
#df_2019_schedule = pd.read_excel(xlsx, "Regular2018_19")
df_2019_schedule = pd.read_excel(xlsx, "Regular2019_20")
#df_2018_standings = pd.read_excel(xlsx, "2017-18_Final_Standings")
#df_2018_standings = pd.read_excel(xlsx, "2018-19_Final_Standings")
df_2018_standings = pd.read_excel(xlsx, "2019-20_Final_Standings")

# Team info lists: [Name, PrevGF, PrevGA, W, L, OT, Division, PTS, PCT, GF, GA, GP]
teams = [['Boston Bruins           ', 227, 174, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Buffalo Sabres          ', 195, 217, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Detroit Red Wings       ', 145, 267, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Florida Panthers        ', 231, 228, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0],
         ['Montreal Canadiens      ', 212, 221, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Ottawa Senators         ', 191, 243, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Tampa Bay Lightning     ', 245, 195, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Toronto Maple Leafs     ', 238, 227, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0],
         ['Carolina Hurricanes     ', 222, 193, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Columbus Blue Jackets   ', 180, 187, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['New Jersey Devils       ', 189, 230, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['New York Islanders      ', 192, 193, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0],
         ['New York Rangers        ', 234, 222, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Philidelphia Flyer      ', 232, 195, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Pitsburgh Penguins      ', 224, 196, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0], ['Washington Capitals     ', 240, 215, 0, 0, 0, 'Eastern ', 0, 0, 0, 0, 0],
         ['Chicago Blackhawks      ', 212, 218, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Colorado Avalanche      ', 237, 191, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Dallas Stars            ', 180, 177, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Minnestoa Wild          ', 220, 220, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0],
         ['Nashville Predators     ', 215, 217, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['St. Louis Blues         ', 225, 193, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Winnipeg Jets           ', 215, 203, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Anaeheim Ducks          ', 187, 226, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0],
         ['Arizona Coyotes         ', 195, 187, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Calgary Flames          ', 210, 215, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Edmonton Oilers         ', 225, 217, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Los Angeles Kings       ', 178, 212, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0],
         ['San Jose Sharks         ', 182, 225, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Vancouver Canucks       ', 228, 217, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0], ['Las Vegas Golden Knights', 227, 211, 0, 0, 0, 'Western ', 0, 0, 0, 0, 0]]
for i in df_2018_standings.index:
    teams[i][0] = df_2018_standings['Team'][i]
    teams[i][1] = df_2018_standings['GF'][i]
    teams[i][2] = df_2018_standings['GA'][i]
    teams[i][6] = df_2018_standings['Location'][i]


# teams[0][0] = "Boston BRUINS           "

# Games - HomeTeam, H_Goals, AwayTeam, A_Goals, Status(OT, RG)
# subroutines
def playGame(teamA, teamH):
    '''Initialization'''
    # variables
    spacer = ""
    teamAName = teamA[0]
    teamAOff = teamA[1]     # GF
    teamADef = teamA[2]     # GA
    teamHName = teamH[0]
    teamHOff = teamH[1]
    teamHDef = teamH[2]
    scoreA = 0
    scoreH = 0
    overtime = 0

    # subroutines
    def goalScoringDistribution():  # Goal scoring distribution based on actual NHL stats.
        score = 0  # initialize variable
        #score = random.gammavariate(3, 0.3) + random.normalvariate(1, 1.1) + random.uniform(0.2, 2.2)
        #score = random.randint(0, 7)
        score = random.random()*7
        return score
    '''Execution'''
    scoreH = int((teamHOff/teamAOff) * (teamADef/teamHDef) * goalScoringDistribution() - 0.1)
    scoreA = int((teamAOff/teamHOff) * (teamHDef/teamAOff) * goalScoringDistribution() - 0.3)
    if scoreH < 0:  # No negative scores
        scoreH = 0
    if scoreA < 0:
        scoreA = 0

    # Tiebreak
    if scoreA == scoreH:
        otscore = 0
        overtime += 1
        otScore = random.uniform(0, (teamHOff / teamADef) + (teamAOff / teamHDef))
        if otScore < teamAOff / teamHDef - 0.1:
            scoreH += 1
        elif otScore > teamAOff / teamHDef + 0.1:
            scoreA += 1
        elif otScore < teamAOff / teamHDef:
            scoreH += 1
            overtime += 1
        else:
            scoreA += 1
            overtime += 1
    return [overtime, scoreA, scoreH]

'''Execution'''
##
## use schedule from excel and run full 82 game schedule for each team
##
# use the match for the index of what team to update stats
#   Team will be from the schedule and returns the avg of GF/GA and index
def Check_Avg(Team):
    for j in df_2018_standings.index:
        match = re.match(Team, df_2018_standings['Team'][j])
        if match:
            # print("Team: ", Team, " Avg: ", df_2018_standings['GF'][j]/df_2018_standings['GA'][j])
            return(df_2018_standings['GF'][j]/df_2018_standings['GA'][j], j)
# provide a counter to allow to play same season more then once
f = open("/Library/WebServer/CGI-Executables/NHL_SIMULATION/SCHED/"+dt_run+"SCHED.txt", "w")
#f.write("<table border=1  class='dataframe'>\n")
for z in range(game_loop):
  for i in df_2019_schedule.index:
    date_of_game = df_2019_schedule['Date'][i]
    Home_Avg, teamH = Check_Avg(df_2019_schedule['Home'][i])
    Away_Avg, teamA = Check_Avg(df_2019_schedule['Away'][i])
    if teamA != teamH:
        # play a game
        gameResult = playGame(teams[teamA], teams[teamH])
        # convert game result list to variables
        overtime = gameResult[0]
        scoreA = gameResult[1]
        scoreH = gameResult[2]
        # pull names from team list
        teamHName = teams[teamH][0]
        teamAName = teams[teamA][0]

        # update teams' W-L records
        if scoreA > scoreH and overtime == 0:
            teams[teamA][3] += 1       # wins away
            teams[teamA][7] += 2       # pts away
            teams[teamH][4] += 1       # loses home
            teams[teamA][9] += scoreA  # GF away
            teams[teamH][9] += scoreH  # GF home
            teams[teamA][10] += scoreH # GA home
            teams[teamH][10] += scoreA # GA away
            teams[teamA][11] += 1      # games played away
            teams[teamH][11] += 1      # games played home
        elif scoreA > scoreH and overtime > 0:
            teams[teamA][3] += 1       # wins away
            teams[teamA][7] += 2       # PTS away
            teams[teamH][5] += 1       # OTL home
            teams[teamH][7] += 1       # PTS home
            teams[teamA][9] += scoreA  # GF away
            teams[teamH][9] += scoreH  # GF home
            teams[teamA][10] += scoreH # GA away
            teams[teamH][10] += scoreA # GA home
            teams[teamA][11] += 1      # Games away
            teams[teamH][11] += 1      # Games home
        elif scoreH > scoreA and overtime == 0:
            teams[teamH][3] += 1       # wins home
            teams[teamH][7] += 2       # PTS home
            teams[teamA][4] += 1       # loses away
            teams[teamA][9] += scoreA  # GF away
            teams[teamH][9] += scoreH  # GF home
            teams[teamA][10] += scoreH # GA away
            teams[teamH][10] += scoreA # GA home
            teams[teamA][11] += 1      # games away
            teams[teamH][11] += 1      # games home
        elif scoreH > scoreA and overtime > 0:
            teams[teamH][3] += 1       # wins home
            teams[teamH][7] += 2       # PTS home
            teams[teamA][5] += 1       # OTL away
            teams[teamA][7] += 1       # PTS away
            teams[teamA][9] += scoreA  # GF away
            teams[teamH][9] += scoreH  # GF home
            teams[teamA][10] += scoreH # GA away
            teams[teamH][10] += scoreA # GA home
            teams[teamA][11] += 1      # games away
            teams[teamH][11] += 1      # games home
        else:
            print('Error 704')  # Error 704: inconclusive game result (score or OT status)

    if overtime==0:
      if scoreA>scoreH:
        statusX = "RG"
        #continue
        #print(date_of_game, teamAName, ' (Away):', scoreA, teamHName, ' (Home):', scoreH, " RG<br>")
      elif scoreH>scoreA:
        statusX = "RG"
        #continue
        #print(date_of_game, teamAName, ' (Away):', scoreA, teamHName, ' (Home):', scoreH, " RG<br>")
      else:
        print('Error 701') #Error 701: tie game result (reg)
    elif overtime==1:
      if scoreA>scoreH:
        statusX = "OT"
        #continue
        #print(date_of_game, teamAName, ' (Away):', scoreA, teamHName, ' (Home):', scoreH, " OT<br>")
      elif scoreH>scoreA:
        statusX = "OT"
        #continue
        #print(date_of_game, teamAName, ' (Away):', scoreA, teamHName, ' (Home):', scoreH, " OT<br>")
      else:
        print('Error 702') #Error 702: tie game result (OT)
    elif overtime==2:
      if scoreA>scoreH:
        statusX = "SO"
        #continue
        #print(date_of_game, teamAName, ' (Away):', scoreA, teamHName, ' (Home):', scoreH, " SO<br>")
      elif scoreH>scoreA:
        statusX = "SO"
        #continue
        #print(date_of_game, teamAName, ' (Away):', scoreA, teamHName, ' (Home):', scoreH, " SO<br>")
      else:
        print('Error 703') #Error 703: tie game result (SO)
    else:
      print('Error 700') #Error 700: overtime variable is invalid'''
    #teamName2 = {:20}.format(teamAName)
    f.write("<tr><td>"+'{:30}'.format(teamAName)+'</td><td align=center>'+str(scoreA)+"</td><td align=left>"+'{:30}'.format(teamHName)+"</td><td align=center>"+str(scoreH)+"</td><td align=center>"+statusX+"</td></tr>\n")
    #f.write('{:30}'.format(teamAName)+' '+str(scoreA)+"     "+'{:30}'.format(teamHName)+' '+str(scoreH)+"  "+statusX+"\n")
    #f.write('{:30}'.format(teamAName)+' (Away) : '+str(scoreA)+" "+'{:30}'.format(teamHName)+' (Home) : '+str(scoreH)+"  "+statusX+"\n")

f.close()
# display teams' W-L records
best_points = 0
best_team = ""
#print(' ')
#print('2021 Final Standings')
for i in range(0, 31):
    # PCT (8) is the PTS(7)/(GP*2)(11)
    teams[i][8] = "{:.3f}".format(teams[i][7]/(teams[i][11]*2))
    if teams[i][7] > best_points:
        best_points = teams[i][7]
        best_team = teams[i][0]
        
df = pd.DataFrame(teams)
pd.options.display.max_columns = None
pd.options.display.width = None
#
# add up GF + GA to see if random is set nicely
#
TG1 = 0
TG2 = 0
for ind in df.index:
    TG1 = TG1 + df[1][ind] + df[2][ind]
    TG2 = TG2 + df[9][ind] + df[10][ind]

lst = df[[0,3,4,5,7,8,9,10,11]].sort_values(7,ascending=False).values.tolist()

total_rows = len(lst)
total_columns = len(lst[0])

df.columns = ['Team', 'P_GF', 'P_GA', 'Wins', 'Loses', 'OTL', 'Loc', 'Points', '%Points', 'GF', 'GA', 'Games']
html = df[['Team', 'Wins', 'Loses', 'OTL', 'Loc', 'Points', '%Points', 'GF', 'GA', 'Games']].sort_values(['Points'],ascending=False).to_html(index=False)

#
# Generate my own formatted HTML because to_html doesn't give you easy fliexibility on formatting
#
print("<center><font size=5><color=red><input type='submit' value='Re-run the Simulation' style='font-size : 30px;height:20px; width:100%;height:50px;color:red;>'</input><br>")
header = "<b><font size=4><center><p style='color:blue;'> NHL Season Simulator v1.0 - Final Standings @Copyright Wilky Consultants Inc.<p style='color:green;'>Simulations="+str(simulation_ctr)+" - Last run: "+dt_run+" EST "+"<br>Based on 2019-20 Season Schedule<br><img src='/NHL.png' width=100 height=80></p></b><table border='1' class='dataframe'>\n"
print(header)
#print("<center><font size=4><input type='submit' value='Rerun Simulation' style='font-size : 30px;height:20px; width:100%;height:50px;>'</input><br>")
print("<a href='sql_report_by_count_sorted.py' target=_blank>Finish by Count / </a><a href='sql_report_by_pct_sorted.py' target=_blank>Finish by % / </a><a href=NHL_games_history_pct.py?sort_field=pct_points>  Sort All on Pct</a><a href=web_dropdown1.py target=_blank> / Select Sim</a>")
header = "<thead><tr style='text-align: center;'><th>Logo</th><th>Team</th><th>Wins</th><th>Loses</th><th>OTL</th><th>Conference</th><th>Points</th><th>%Points</th><th>GF</th><th>GA</th><th>Games</th></tr></thead><tbody>\n"
print(header)
ctr = 0
for ind in df.sort_values(['Points'], ascending=False).index:
     ctr=ctr+1
     (TM2, rest) = df['Team'][ind].split(maxsplit=1)
     if df['Team'][ind] == "New York Rangers":
        TM = "Rangers"
     elif df['Team'][ind] == "New York Islanders":
        TM = "Islanders"
     elif df['Team'][ind] == "New Jersey Devils":
        TM = "Devils"
     else:
        TM = TM2

     print("<tr><td><center><a href=NHL_games_history.py?t="+TM+"&sort_field=Fposition><img src='/"+TM+".png' width=40 height=30></a></td><td><a href=NHL_games.py?t="+TM+"&dt_run="+dt_run+" target=_blank>"+df['Team'][ind]+"</a></td><td align=center>"+str(df['Wins'][ind])+"</td><td align=center>"+str(df['Loses'][ind])+"</td><td align=center>"+str(df['OTL'][ind])+"</td><td align=center>"+str(df['Loc'][ind])+"</td><td align=center>"+str(df['Points'][ind])+"</td><td align=center>"+str(df['%Points'][ind])+"</td><td align=center>"+str(df['GF'][ind])+"</td><td align=center>"+str(df['GA'][ind])+"</td><td align=center>"+str(df['Games'][ind])+"</td></tr>\n")
# set up the fields for the database
     dt = dt_run
     team = df['Team'][ind]
     wins = int(df['Wins'][ind])
     loses = int(df['Loses'][ind])
     otl = int(df['OTL'][ind])
     conference = df['Loc'][ind]
     points = int(df['Points'][ind])
     pct_points = df['%Points'][ind]
     gf = int(df['GF'][ind])
     ga = int(df['GA'][ind])
     games = int(df['Games'][ind])
     Fposition = int(ctr)
     sql_insert_query = """ INSERT INTO NHL_Season
                   (id, dt, team, wins, loses, otl, conference, points, pct_points, gf, ga, games, Fposition) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
     insert_tuple_1 = (None, dt, team, wins, loses, otl, conference, points, pct_points, gf, ga, games, Fposition)
     mycursor = mydb.cursor()
     mycursor.execute(sql_insert_query, insert_tuple_1)
     mydb.commit()
     if ctr == 1:
        sql_insert_query = """ INSERT INTO NHL_counter
                   (id, dt) VALUES(%s,%s)"""
        insert_tuple_1 = (None, dt)
        mycursor = mydb.cursor()
        mycursor.execute(sql_insert_query, insert_tuple_1)
        mydb.commit()
mydb.close()
print("</form>")

