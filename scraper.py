from bs4 import BeautifulSoup as bs
import requests

class GitHubWebScraper():

    global url 
    url = "https://github.com/"

    def GetWebPageData(username):
        finalUrl = url + username
        GitHubWebScraper.ScrapeInformation()
        return finalUrl
        
    def ScrapeInformation():
        return