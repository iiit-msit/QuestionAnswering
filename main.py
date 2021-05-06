import codecs
f=codecs.open("/Users/srinathesv/Desktop/a1.htm", 'r')

from bs4 import BeautifulSoup

soup = BeautifulSoup(f, 'html.parser')
#print(soup.prettify())

#print(soup.body.get_text())

s1 = soup.body.get_text()
print(s1) 

file1 = open('/Users/srinathesv/Desktop/a1.txt', 'w')
file1.write(s1)
file1.close()

'''
file1 = open('a1.txt', 'r')
print(file1.read())
file1.close()
'''
