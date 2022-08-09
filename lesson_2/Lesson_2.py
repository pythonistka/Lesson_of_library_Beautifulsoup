import requests
from bs4 import BeautifulSoup

# сохраним индексную страницу, на которой находятся ссылки на категории продуктов
url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

# заголовки (добавляем accept и user-agent, для того, чтобы показать сайту, что мы не бот, а обычный пользователь)
# копируем из браузера во вкладке network в любом из get запросов
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
# req будет возвращать результат работы метода get
req = requests.get(url, headers=headers)
src = req.text

# убедились, что получили код страницы
# print(src)
# сохраним страницу в файл
with open("index.html", "w", encoding='utf-8-sig') as file:
    file.write(src)