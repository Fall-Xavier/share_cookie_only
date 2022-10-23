import re, requests, bs4, json
from bs4 import BeautifulSoup as parser
ses=requests.Session()
token = "token kamu"
cok = "cookie kamu"
cookie = {"cookie":cok}

link = input("masukan link : ")
limit = int(input("masukan limit : "))
try:
	n=0
	for z in range(limit):
		n+=1
		url = parser(ses.get(f"https://m.facebook.com/sharer/sharer.php?u={link}",cookies=cookie).text,"html.parser")
		for x in url.find_all("input"):
			data.update({x.get("name"):x.get("value")})
		res = ses.post("https://m.facebook.com/v2.3/dialog/share/submit", data=data,cookies=cookie)
		if "Harap tutup tab ini untuk melanjutkan." in res.text:
			print(f"{n}. berhasil membagikan postingan")
		else:
			exit("gagal membagikan, kemungkinan cookie invalid")
except Exception as e:
	print(e)
