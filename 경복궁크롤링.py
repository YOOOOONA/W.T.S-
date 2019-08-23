# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:52:38 2019

@author: 융
"""

from bs4 import BeautifulSoup
import requests
URL="http://www.royalpalace.go.kr/content/board/"
URL1=URL+"list.asp"  #경복궁 공지사항 탭
ur_f="view.asp?seq="
ur_m="&page=&c1=&c2="

html = requests.get(URL)
#한글 깨지지 않게 하는 방법
soup = BeautifulSoup(html.content.decode('euc-kr','replace'))
print(soup.prettify())#태그만 전체 출력
print(soup.title)#<title>문화재청 경복궁</title>
print(soup.title.get_text())#문화재청 경복궁   same as print(soup.title.string) or text도 가능

for i in range(620,640):
    link=URL+ur_f+i+ur_m
    html=requests.get(link)
    soup=BeautfulSoup(html.content.decode('euc-kr','replace'))
    print(soup.)
for link in soup.find_all('a', class_='g_link'):
    url[]
    print(link.get('href'))

"""
한페이지 10개 게시물 링크
view.asp?seq=640&page=&c1=&c2=
view.asp?seq=639&page=&c1=&c2=
view.asp?seq=638&page=&c1=&c2=
view.asp?seq=637&page=&c1=&c2=
view.asp?seq=636&page=&c1=&c2=
view.asp?seq=635&page=&c1=&c2=
view.asp?seq=634&page=&c1=&c2=
view.asp?seq=633&page=&c1=&c2=
view.asp?seq=632&page=&c1=&c2=
view.asp?seq=630&page=&c1=&c2=
"""

for link in soup.find_all('a', class_='page_menu'):
    print(link.get('href'))
"""
페이지 넘기는 링크
/content/board/list.asp?p=p&c1=&c2=&page=1
/content/board/list.asp?p=p&c1=&c2=&page=2
/content/board/list.asp?p=p&c1=&c2=&page=3
/content/board/list.asp?p=p&c1=&c2=&page=4
/content/board/list.asp?p=p&c1=&c2=&page=5
/content/board/list.asp?p=p&c1=&c2=&page=6
/content/board/list.asp?p=p&c1=&c2=&page=7
/content/board/list.asp?p=p&c1=&c2=&page=8
/content/board/list.asp?p=p&c1=&c2=&page=9
/content/board/list.asp?p=p&c1=&c2=&page=10
/content/board/list.asp?p=p&c1=&c2=&page=11
/content/board/list.asp?p=p&c1=&c2=&page=63 #맨 끝으로
"""
 #temper
print("temper:")
tempTable = soup.find_all("td", class_="f11")   

 for i in range(10):
    temp=tempTable[i].text
    high=float(temp[:2])
    low=float(temp[5:7])
    ave=(high+low)/2
    print(ave)
    