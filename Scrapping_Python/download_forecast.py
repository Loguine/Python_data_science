import urllib

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

value = {
    'stnId ': '108'
}

params = urllib.urlencode(value)

url = API + "?" + params
print("url=", url)

data = urllib.urlopen(url).read()
text = data.decode("utf-8")
print(text)
