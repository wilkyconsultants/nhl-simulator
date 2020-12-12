#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
  
print("Content-type: text/html\n\r\n")
import cgi, cgitb
import re

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
dt_run = form.getvalue('dt_run')
print("<b>Games from simulation: ",dt_run,"<br></b>")
print("</pre><table border=1  class='dataframe'>\n")
print("<tr><td align=center><b>Visitng Team</td><td align=center><b>Goals</td><td align=center><b>Home Team</td><td align=center><b>Goals</td><td align=center><b>OT</td></tr>\n")
for line in open("/Library/WebServer/CGI-Executables/NHL_SIMULATION/SCHED/"+dt_run, 'r'):
        line = line.replace("RG", "  ")
        print(line)
        if line == None:
            print('no games found')
