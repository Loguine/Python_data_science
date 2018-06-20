import urllib

# define the directory #


url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# download files#

urllib.urlretrieve(url, savename)
print("saved!!")
