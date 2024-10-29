from bs4 import BeautifulSoup



def read_file():
    file = open('NAVIGATING Bs4 SOUP/GOING DOWN/three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# .contents             --- returns us direct children of the said tag

head = soup.head
body = soup.body

# children = [child for child in body.contents if child != '\n']



children = [child for child in body.contents if child != '\n' and not str(child).isspace()]
# print(len(children))


# .descendants  -- returns us all the children of the said tag -- generator


for index, child in enumerate(soup.head.descendants):
    print(index)
    print(child if child != '\n' else '')

