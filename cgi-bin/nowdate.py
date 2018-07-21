import datetime as dt

html_body="""
<html><body>
%d/%d/%d %d:%d:%d
</body></html>"""

now = dt.datetime.now()

print("Content-type: text/html")
print(html_body % (now.year, now.month, now.day, now.hour, now.minute, now.second))