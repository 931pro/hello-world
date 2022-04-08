import re
from bs4 import BeautifulSoup
import requests


def weibo_hot():
    url='https://tophub.today/n/KqndgxeLl9'
    headers = {
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",

          }
    p=re.compile(r'<a.*?>(.*?)</a.*?>')
    p2=re.compile(r'>(.*?)<')
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    main_page=BeautifulSoup(resp.text,'html.parser')
    lis=main_page.find_all('td',class_='al')
    ans=[]
    for i in lis:
        j=str(i)
        j=p.search(j).group(0)
        j=p2.search(j).group(0)
        j=j.replace('<','')
        j=j.replace('>','')
        if(len(ans)<10):
          ans.append(j)
    return ans