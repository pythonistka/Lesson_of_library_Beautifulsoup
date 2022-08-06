# pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup
# открываем файл страницы
with open("index.html", encoding='utf-8') as file:
    src = file.read()
# print(src)

# нам нужно скормить код нашей страницы библиотеке BeautifulSoup, чтобы мы могли пользоваться ее методами для
# извлечения информации
# обозначим переменную soup и создадим объект класса BeautifulSoup, в качестве параметров он принимает нашу
# переменную с кодом src, а вторым параметром указываем название парсера, который будет использован (lxml)
# (устанавливаем через терминал аналогично BeautifulSoup)
soup = BeautifulSoup(src, "lxml")

# получаем информацию из тега title
title = soup.title
print(title)
# для того, чтобы получить содержимое тега, используем метод text
print(title.text)
# либо string
print(title.string)

# [*] Методы .find и .find_all()
# работают на странице сверху вниз
# для демонстрации работы методов добавим в html еще одид заголовок h1
page_h1 = soup.find("h1")
# find находит и забирает данные только из самого первого заголовка с тегом h1
print(page_h1)

page_all_h1 = soup.find_all("h1")
# find_all находит и забирает данные из всех заголовков с тегом h1 и записывает их в список
print(page_all_h1)
for item in page_all_h1:
    print(item.text)

# Помимо поиска по тегу, мы можем конкретизировать запрос, указывая атрибут тега, например класс
# Пример: получим имя пользователя, которое лежит в теге span, внутри тега div, с классом user__name
user_name = soup.find("div", class_="user__name")
# если указываем просто user_name мы получаем блок кода целиком, чтобы получить текск, добавляем метод text,
# а чтобы обрезать ненужные пробелы применяем strip и получаем чистый текст
print(user_name.text.strip())

#  Можно применять связку из методов шагая вглубь по коду
user_name = soup.find("div", class_="user__name").find("span").text
# в данном случае можно не указывать, что мы ищем данные непосредственно в теге div, но в таком случае, если класс
# user__name используется где то еще на странице, то метод find будет выводить данные, идущие первыми по коду,
# с выбранным классом без привязки к конкертному тегу
print(user_name)

# Вторым способом задания атрибутов для фильтрации поиска является передача словаря в котором с помощью пары
# ключ:значение указываем параметры отбора
user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text
# удобство данного способа заключается в том, что если нам нужны какие то жесткие требования отбора, мы сразу же
# через запятую можем передать дополнительный параметр например в виде атрибута id
print(user_name)

# с помощью метода find_all соберем все span теги из блоков с классом user__info
find_all_spans_in_user_info = soup.find("div", {"class": "user__info"}).find_all("span")
print(find_all_spans_in_user_info)
for item in find_all_spans_in_user_info:
    print(item.text)
# так как это обычный список мы можем обращаться к его элементам по индексу
print(find_all_spans_in_user_info[0].text)
print(find_all_spans_in_user_info[2].text)

# спарсим ссылки на соцсети
social_links = soup.find("div", {"class": "social__networks"}).find_all("a")
print(social_links)
for item in social_links:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")