# pip install beautifulsoup4 lxml
from bs4 import BeautifulSoup
# открываем файл страницы
with open("index.html") as file:
    src = file.read()
# print(src)

# нам нужно скормить код нашей страницы библиотеке BeautifulSoup, чтобы мы могли пользоваться ее методами для
# извлечения информации
# обозначим переменную soup и создадим объект класса BeautifulSoup, в качестве параметров он принимает нашу
# переменную с кодом src, а вторым параметром указываем название парсера, который будет использован (lxml)
# (устанавливаем через терминал аналогично BeautifulSoup)
soup = BeautifulSoup(src, "lxml")
