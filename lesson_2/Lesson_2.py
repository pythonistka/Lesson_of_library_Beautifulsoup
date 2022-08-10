import requests
from bs4 import BeautifulSoup
import json

# # сохраним индексную страницу, на которой находятся ссылки на категории продуктов
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# # заголовки (добавляем accept и user-agent, для того, чтобы показать сайту, что мы не бот, а обычный пользователь)
# # копируем из браузера во вкладке network в любом из get запросов
# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
# # req будет возвращать результат работы метода get
# req = requests.get(url, headers=headers)
# src = req.text
#
# # убедились, что получили код страницы
# # print(src)
# # сохраним страницу в файл
# with open("index.html", "w", encoding='utf-8-sig') as file:
#     file.write(src)

# откроем прочитаем наш файл и сохраним код страницы в переменную
with open("index.html", encoding='utf-8-sig') as file:
    src = file.read()

# создадим объект soup и передадим в него в качестве параматера нашу переменную src, парсер lxml и приступим к сборке
soup = BeautifulSoup(src, "lxml")
# у всех ссылок на группы товаров один и тот же класс, по ним мы и соберем ссылки
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

# забираем из всей информации наименовние блоков и ссылки на них, к href добавляем доменное имя https://health-diet.ru/
all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_href = "https://health-diet.ru/" + item.get("href")

    all_categories_dict[item_text] = item_href

# сохраним в json файл
with open("all_categories_dict.json", "w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)