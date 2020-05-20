import re
import requests
from bs4 import BeautifulSoup
import os
from user_agent import generate_user_agent

headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

print("Вставьте любую ссылку на категорию Ozon.ru, в которой вы хотите скачать фотографии в высоком качестве,\n"
      "Например, https://www.ozon.ru/highlight/37196/ или https://www.ozon.ru/category/antivirusy-32647/eset-149974849/")

URL = input("Введите URL: ")
name_folder = input("Введите название папки: ")
os.mkdir(name_folder)
page = requests.get(URL.strip(), timeout=5, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('img', src=re.compile(('https:\/\/\w+.\w+.\w+\/\w+\/[\w+-]+\/\w+\/\w+\.\w+')))
print(results)

print(type(results))
print(len(results))

count = 0

for result in results:
    link = result['src']
    link = link.replace("c250", "c1200")  # Получаем ссылку на фото большого размера (из карточки товара)
    print(link)
    img_data = requests.get(link)
    print(img_data.content)

    with open(name_folder + "/" + str(count) + ".jpg", "wb") as handler:
        handler.write(img_data.content)
    count += 1
