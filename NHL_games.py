#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

print("Content-type: text/html\n\r\n")
import cgi, cgitb 
import re

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
t = form.getvalue('t')
dt_run = form.getvalue('dt_run')
if t == "St.":
	x = "St."
	t = "St. Louis"
else:
        x = t[0:len(t)]
png = "<center><img src='/"+x+".png' width=180 height=150><br>"+dt_run
print(png)
f = "SCHED/"+dt_run+"SCHED.txt"
#print("<p style='color:red'><br><br><p style='color:blue'><p style='font-family: monospace;'><pre>")
print("</pre><table border=1  class='dataframe'>\n")
print("<tr><td align=center><b>Visitng Team</td><td align=center><b>Goals</td><td align=center><b>Home Team</td><td align=center><b>Goals</td><td align=center><b>OT</td></tr>\n")
for line in open(f, 'r'):
    if re.search(t, line):
        line = line.replace("RG", "  ")
        print(line)
        #print(line,"<br>")
        if line == None:
            print('no games found')
