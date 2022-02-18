from bs4 import BeautifulSoup as bs
import requests

class GitHubWebScraper():

    global url 
    
    url = "https://github.com/"

    def GetWebPageData(username):
 
        finalURL = url + username

        r = requests.get(finalURL)
        r.encoding = r.apparent_encoding
        content = r.text
        r.raise_for_status()
        soup = bs(content, "html.parser")
        return soup
        
        
    def ScrapeInformation(soup):
        profile_image = soup.find('img', class_ = "avatar avatar-user width-full border color-bg-default")["src"]
        name = soup.find('span', {"itemprop" : "name"}).get_text()
        followersArray = soup.find_all("span", class_ = "text-bold color-fg-default")
        followers, following = followersArray
        followers = followers.string
        following = following.string
        contributions = soup.find('h2', class_ = "f4 text-normal mb-2").string
        return name, profile_image, followers, following, contributions
        