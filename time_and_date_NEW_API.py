import requests
import json

api_key = "a95770827a9048f6a3cc3b236ee1b6db"

base_url = "https://api.ipgeolocation.io/timezone"
complete_url = base_url + '?apiKey=' + api_key + '&tz=America/New_York'

response = requests.get(complete_url);

x = response.json()

y = x["date_time_txt"]


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
