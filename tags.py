

from bs4 import BeautifulSoup

def read_file():
    file = open('tags.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#Accessing tags
meta = soup.meta


# modify arrtributes

body = soup.body

body['style'] = 'some style'

print(body['class'])







