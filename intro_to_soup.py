
from bs4 import BeautifulSoup


def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data

html_file = read_file()

soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())







