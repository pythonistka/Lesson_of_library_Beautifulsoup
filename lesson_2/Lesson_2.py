import requests
from bs4 import BeautifulSoup
import json
import csv

# # # сохраним индексную страницу, на которой находятся ссылки на категории продуктов
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
# #
# # # заголовки (добавляем accept и user-agent, для того, чтобы показать сайту, что мы не бот, а обычный пользователь)
# # # копируем из браузера во вкладке network в любом из get запросов
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
# # # req будет возвращать результат работы метода get
# req = requests.get(url, headers=headers)
# src = req.text
# #
# # # убедились, что получили код страницы
# # # print(src)
# # # сохраним страницу в файл
# with open("index.html", "w", encoding='utf-8-sig') as file:
#     file.write(src)
#
# # # откроем прочитаем наш файл и сохраним код страницы в переменную
# with open("index.html", encoding='utf-8-sig') as file:
#     src = file.read()
# #
# # # создадим объект soup и передадим в него в качестве параматера нашу переменную src, парсер lxml и приступим к сборке
# soup = BeautifulSoup(src, "lxml")
# # # у всех ссылок на группы товаров один и тот же класс, по ним мы и соберем ссылки
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
# #
# # # забираем из всей информации наименовние блоков и ссылки на них, к href добавляем доменное имя https://health-diet.ru/
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#
#     all_categories_dict[item_text] = item_href
# #
# # # сохраним в json файл
# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

# загрузим файл в пременную all_categories
with open("all_categories_dict.json") as file:
    all_categories = json.load(file)

# создаем цикл, на каждой итерации которого будем заходить на новую страницу категории, собирать с нее данные о всех
# товарах и химическом составе и записывать всё это в файл
count = 0
for category_name, category_href in all_categories.items():
#    создадим список из символов, которые хотим заменить, прописываем цикл, если один из символов содержится в имени
#    категории, то заменяем его на нижний пробел
    if count == 0 or count == 1:
        rep = [",", " ", "-", "'"]
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, "_")
        # переходим к запросам на странице (раскоментируем заголовки, чтоб снова можно было их использовать), сохраняем в
    # переменную src результат
        req = requests.get(url=category_href, headers=headers)
        src = req.text
        #  сохраняем страницу под именем категории (для чистоты проекта создадим папку data и все страницы с файлами
    #  будем сохранять в нее
        with open(f"data/{count}_{category_name}.html", "w", encoding='utf-8') as file:
            file.write(src)

        # собираем данные со страницы(откроем и сохраним код страницы в переменную
        with open(f"data/{count}_{category_name}.html", encoding='utf-8') as file:
            src = file.read()
        # создаем объект soup
        soup = BeautifulSoup(src, "lxml")
        #  собираем заголовки в таблице
        table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
        product = table_head[0].text
        calories = table_head[1].text
        proteins = table_head[2].text
        fats = table_head[3].text
        carbohydrates = table_head[4].text

        with open(f"data/{count}_{category_name}.csv", "w", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    product,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )


        count += 1