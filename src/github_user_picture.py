import requests
from bs4 import BeautifulSoup as bs

def get_picture_link(github_user):
  page = requests.get(f'https://github.com/{github_user}')
  site = bs(page.content, 'html.parser')
  picture_link = site.find('img', {'class' : "avatar avatar-user width-full border color-bg-default"})['src']
  return picture_link


user = str(input("Input Github user: "))
print(f'{user} profile picture link: \n{get_picture_link(user)}')

