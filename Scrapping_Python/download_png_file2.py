import urllib

# defined url and directory#


url = "http://uta.pw/shodou/img/28/214.png"
save_name = "test2.png"

# download#

mem = urllib.urlopen(url).read()

# save as a file#
with open(save_name, mode="wb") as f:
    f.write(mem)
    print("saved!!!!!")
