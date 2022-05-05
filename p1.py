# import requests
# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL)
# print(r.content)
from bs4 import BeautifulSoup
import requests
  
# creating function
def scrape_info(url):
      
    # getting the request from url
    r = requests.get(url)
      
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
      
    # finding meta info for title
    for title in s.find_all('title'):
        print(title.get_text())
      
    # finding meta info for views
    views = s.find("span", class_="short-view-count").text
    print(views)
    # finding meta info for likes
    likes = s.find("span", class_="like-button-renderer").span.button.text
      
    # saving this data in dictionary
    data = {'title':title, 'views':views, 'likes':likes}
      
    # returning the dictionary
    return data
  
# main function
if __name__ == "__main__":
      
    # URL of the video
    url ="https://www.youtube.com/watch?time_continue=17&v=2wEA8nuThj8"
      
    # calling the function
    data = scrape_info(url)
      
    # printing the dictionary
    print(data)