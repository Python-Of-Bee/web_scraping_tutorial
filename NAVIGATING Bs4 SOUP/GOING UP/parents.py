from bs4 import BeautifulSoup



def read_file():
    file = open('NAVIGATING Bs4 SOUP/GOING DOWN/three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# .parents              --- returns a list ( generator )  of parents

link = soup.a




for parent in link.parents:
    print(parent)
