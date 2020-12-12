#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

print("Content-type: text/html\n\r\n")
import cgi;
import cgitb;cgitb.enable()
import os
print("<p>Hello world!<br>")
y = int(3.44)
print(y, "<br>")
f = open("test.txt", "w")
f.write("test")
f.close()
os.system('ls -l')
