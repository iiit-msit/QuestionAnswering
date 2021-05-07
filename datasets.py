# Import libraries
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse


# Set for storing urls with same domain
links_intern = set()
input_url = "https://en.wikipedia.org/wiki/Web_scraping"
depth = 10

# Set for storing urls with different domain
links_extern = set()


# Method for crawling a url at next level
def level_crawler(input_url):
	temp_urls = set()
	current_url_domain = urlparse(input_url).netloc

	# Creates beautiful soup object to extract html tags
	beautiful_soup_object = BeautifulSoup(
		requests.get(input_url).content, "lxml")

	# Access all anchor tags from input
	# url page and divide them into internal
	# and external categories
	for anchor in beautiful_soup_object.findAll("a"):
		href = anchor.attrs.get("href")
		if(href != "" or href != None or href != "https://en.wikipedia.org/w/index.php.txt"):
			href = urljoin(input_url, href)
			href_parsed = urlparse(href)
			href = href_parsed.scheme
			href += "://"
			href += href_parsed.netloc
			href += href_parsed.path
			final_parsed_href = urlparse(href)
			is_valid = bool(final_parsed_href.scheme) and bool(
				final_parsed_href.netloc)
			if is_valid:
				# if current_url_domain not in href and href not in links_extern:
				# 	print("Extern - {}".format(href))
				# 	links_extern.add(href)
				if current_url_domain in href and href not in links_intern:
					# print("Intern - {}".format(href))
					links_intern.add(href)
					temp_urls.add(href)
					response=requests.get(href)
					print(href)
					filename = href.rsplit('/', 1)[-1]+".txt"
					with open(filename, "w") as file:
						file.write(str(response.content))
	# print(len(temp_urls))
	# for index, url in enumerate(temp_urls):
		
		# print(url)
	#print(len(temp_urls))			
	return temp_urls


if(depth == 0):
	response=requests.get(input_url)
	filename = input_url.rsplit('/wiki/')[-1]+".txt"
	with open(filename, "w") as file:
		file.write(str(response.content))
	# print("Intern - {}".format(input_url))

elif(depth == 1):
	level_crawler(input_url)
	response=requests.get(input_url)
	filename = input_url.rsplit('/wiki/')[-1]+".txt"
	with open(filename, "w") as file:
		file.write(str(response.content))

	

else:
	# We have used a BFS approach
	# considering the structure as
	# a tree. It uses a queue based
	# approach to traverse
	# links upto a particular depth.
	queue = []
	queue.append(input_url)
	for j in range(depth):
		for count in range(len(queue)):
			url = queue.pop(0)
			urls = level_crawler(url)
			response=requests.get(url)
			filename = url.rsplit('/wiki/')[-1]+".txt"
			with open(filename, "w") as file:
				file.write(str(response.content))
			for i in urls:
				queue.append(i)

	





















# # from bs4 import BeautifulSoup
# # import urllib.request
# # import re
# # r=urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page').read()
# # soup = BeautifulSoup(r,"lxml")
# # #print(soup.prettify()[:100])
# # for link in soup.find_all('a'):
# #     print(link.get('href'))

# # print(soup.get_text())
# # print(soup.prettify())


# # #for link in soup.find_all('a',attrs={'href':re.compile("^http")}):
# #     #print(link)

# # file  = open ("parsed_data.txt","w")
# # for link in soup.find_all('a',attrs={'href':re.compile("^http")}):
# #     soup_link = str(link)
# #     print(soup_link)
# #     file.write(soup_link)
# # file.flush()
# # file.close


# # import io, time, json
# import requests
# import re
# # from pathlib import Path
# from bs4 import BeautifulSoup
# def scrape(url):
#     # count = 0
#     # while (count < 5):
#     #     count += 1
#     response=requests.get(url)
#     page=BeautifulSoup(response.content,'html.parser')
#     # print(page)
#     # page = requests.get("url").content
#     # print(page.content)
#     # filename = ""
#     # filename = url.rsplit('/wiki/', 1)[-1]+".txt"
#     # file = open(filename, "w") 
    
#     # file.write(page.get_text()) 
#     # file.close() 
#     url_list = page.findAll('a', attrs={'href': re.compile("^/wiki/")})
#     # print(url_list)
#     res = []
#     for index, url in enumerate(url_list):
#         url = url.get('href')
#         print(url)
        
#         # res.append()
#         # response=requests.get(url)
#         # page=BeautifulSoup(response.content,'html.parser')
#         url = "https://en.wikipedia.org"+url
#         response=requests.get(url)
#         filename = url.rsplit('/wiki/', 1)[-1]+".txt"
#         with open(filename, "w") as file:
            
#             file.write(str(response.content))
#     return 0

# url = "https://en.wikipedia.org/wiki/Web_scraping"

# # count = 0
# print(scrape(url))

# # filename = ""
# #     filename = url.rsplit('/wiki/', 1)[-1]+".txt"
# # ​
# #     file = open(filename, "w") 
# #     page = requests.get("url")
# #     data = page.get_text()
# #     data
# #     file.write(soup.get_text()) 
# #     file.close() 
# #     page = requests.get("url")
