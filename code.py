import requests
from lxml import html  
import csv,os,json

loc = '\links.txt'
loc2 = '\op.txt'

f = open(loc)
f1 = open(loc2,"w+")

line = f.readline()

while line:
    line = line.rstrip('\n')

    url = line
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    t=html.fromstring(response.content)
    title=t.xpath('/html/body/div[1]/div[2]/div/main/article/p/time/text()')
    f1.write(str(title))
    f1.write('\n')
    line = f.readline()
    

print("complete")
f.close()
f1.close()