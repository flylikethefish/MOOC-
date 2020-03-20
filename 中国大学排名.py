import requests
from bs4 import BeautifulSoup
import bs4

def gethtml(url):
    try:
        r=requests.get(url, timeout = 30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('哈哈错了吧')

def transf(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tdss=tr('td')
            ulist.append([tdss[0].string,tdss[1].string,tdss[3].string])

def finalprint(uulist,num1,num2):
    ttlist='{0:{3}^10}\t\t{1:{3}^10}\t\t{2:{3}^10}'
    print(ttlist.format('名次',"学校","分数",chr(12288)))
    for i in range(num1,num2):
        nn = uulist[i]
        print(ttlist.format(nn[0],nn[1],nn[2],chr(12288)))

def main(num1,num2):      #打印前多少名的大学
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    uulist = []
    html = gethtml(url)
    transf(uulist,html)
    finalprint(uulist,num1,num2)

if __name__ == '__main__':
    main(24,46)
