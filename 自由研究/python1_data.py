import requests
from bs4 import BeautifulSoup
import urllib.parse

parao="""
アンガウル島
バベルダオブ島
カヤンゲル島
アラカベサン島
コロール島
ペリリュー島
ソンソロール島
トビ島
マラカル島
カープ島"""
url = "https://ja.wikipedia.org/wiki/%E5%B3%B6%E3%81%AE%E4%B8%80%E8%A6%A7"#wikiのURL
#--------------------スクレイピング-----------
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
a_list = soup.select('ul')
#-------------------ここまで---------------
#print((a_list[35].text+a_list[36].text+a_list[37].text+a_list[38].text
       #+a_list[40].text+a_list[42].text+a_list[43].text+a_list[44].text
       #+a_list[46].text+a_list[47].text).split("\n")+parao.split("\n"))

print(a_list[35].text+a_list[36].text+a_list[37].text+a_list[38].text
       +a_list[40].text+a_list[42].text+a_list[43].text+a_list[44].text
       +a_list[46].text+a_list[47].text+parao)
input("hello")
frein=open("結果.txt","w",encoding="UTF-8")
frein.write(a_list[35].text+a_list[36].text+a_list[37].text+a_list[38].text
       +a_list[40].text+a_list[42].text+a_list[43].text+a_list[44].text
       +a_list[46].text+a_list[47].text+parao
        )
frein.close()
