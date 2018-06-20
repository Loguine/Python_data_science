import urllib

# read data from web#


url = "http://api.aoikujira.com/ip/ini"
res = urllib.urlopen(url)
data = res.read()

# binary to string#
text = data.decode("utf-8")
print(text)
