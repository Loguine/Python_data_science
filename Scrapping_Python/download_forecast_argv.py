import sys
import urllib

if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv<Region Number>")
    sys.exit(0)
regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}

params = urllib.urlencode(values)

url = API + "?" + params
print("url=", url)

data = urllib.urlopen(url).read()
text = data.decode("utf-8")
print(text)
