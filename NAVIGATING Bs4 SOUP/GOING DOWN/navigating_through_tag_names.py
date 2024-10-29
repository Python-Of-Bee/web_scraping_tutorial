from bs4 import BeautifulSoup
import os


def read_file():
    file = open('NAVIGATING Bs4 SOUP/GOING DOWN/three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# example  -- direct

p = soup.p

print(p)



