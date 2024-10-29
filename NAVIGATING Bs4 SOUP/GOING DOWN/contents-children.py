from bs4 import BeautifulSoup



def read_file():
    file = open('NAVIGATING Bs4 SOUP/GOING DOWN/three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')



# tag.contents         -- returns a list of children

head = soup.head
body = soup.body

print(type(head.contents))
print(type(head.children))

for child in head.contents:
    # print(child if child is not None else '', end='\n\n\n\n')
    # print(child if child is not None else '', end='+=+')
    pass





# .children         -- returns an iterator


# for child in body.children:
#     print(child if child is not None else '', end='\n\n\n\n')
