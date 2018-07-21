import datetime
import cgi

html_body="""
<html><body>
今から%s時間後は%s日後です
</body></html>"""

err_body="""
<html><body>
URLの最後に?num=%d形式で入力
</body></html>"""
form = cgi.FieldStorage()
now = datetime.datetime.now()
try:
    hour = now.hour + int(form["num"].value)
except KeyError:
    print("Content-type: text/html")
    print(err_body)
    exit()
day = 0
while hour >= 24:
    hour = hour - 24
    day = day + 1
print("Content-type: text/html")
print(html_body % (form["num"].value,day))
