import requests
from bs4 import BeautifulSoup as bs

github_user = input("Please enter Github usename : ")
url = "https://www.github.com/"+github_user

rs = requests.get(url)

soup = bs(rs.content)

profile_image = soup.find('img' , {'alt' : "Avatar"})['src']

print(profile_image)
