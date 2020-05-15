import re
import requests
from bs4 import BeautifulSoup
region = input("Введите регион для поиска (или help, чтобы посмотреть варианты): ")
if region == 'help':
    print("Посмотрите тут: https://yandex.ru/dev/xml/doc/dg/reference/regions-docpage/")
    region = input("Введите регион для поиска (или help, чтобы посмотреть варианты): ")
your_request = input("Введите ваш запрос: ")

payloads = {'text': your_request, 'lr': region}
r = requests.get('https://www.yandex.ru/search/', params=payloads)

soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('a', href=re.compile('https:\/\/[\w+.-]+?\/?[\w+\/-?.-]+'))
print(results)

with open('result2.txt', 'a') as file:
    for result in results:
        link = result['href']
        print(link)
        file.write(link + '\n')