import datetime
import cgi

html_body="""
<html><body>
num=%s
</body></html>"""

form=cgi.FieldStorage()

print("Content-type: text/html")
print(html_body % form["num"].value)