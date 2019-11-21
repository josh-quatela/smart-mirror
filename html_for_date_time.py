import requests
import json

api_key = "YEY9qVKRfhKy9gdurHwHmUp3JCnPab"

base_url = "https://www.amdoren.com/api/timezone.php"
complete_url = base_url + '?api_key=' + api_key + '&loc=New+York'

response = requests.get(complete_url);

x = response.json()

y = x["time"]


f = open("date_time","w")

m = """
<html>
<head></head>
<body>
<h1 style = "color:white; opacity:10;"><b>"""+ str(y) +"""</b></h1>
</body>
</html>
"""

f.write(m)
f.close()

print(y);
