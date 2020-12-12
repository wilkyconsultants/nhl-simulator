#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3
  
print("Content-type: text/html\n\r\n")

#print("<form action=/cgi-bin/web_dropdown2.py method=post target=_blank style='font-size:30px;width:100%;height:50px;color:blue;'>")
print("<form action=/cgi-bin/NHL_SIMULATION/NHL_games2.py method=post style='font-size:30px;width:100%;height:50px;color:blue;'>")
import os
from lxml import etree
path = '/Library/WebServer/CGI-Executables/NHL_SIMULATION/SCHED/'
listing = os.listdir(path)
sorted_listing=sorted(listing)
print("<select name=dt_run style='font-size:30px;width:100%;height:50px;color:blue;'>")
print("<option value=Choose selected>Choose a simulation and click Submit Button</option>")
for files in sorted_listing:
    if files.startswith('2020'):
        print("<option value=",files,">",files,"</option>")
print("</select>")
print("<input type=submit value=Submit style='font-size:30px;width:100%;height:50px;color:blue;'>")
print("</form>")
