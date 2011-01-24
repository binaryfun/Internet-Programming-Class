import time
import datetime

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print """

<html>
<head>
<title>The Time</titl>
</head>
<body>

<font size=+1>

 """
print "<p>Current time: %s</p>" % time.time()
print "<p>Human Readable: %s</p>" % datetime.datetime.now()
print """
</font>
</body>
</html>
"""


