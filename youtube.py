import youtube_dl, time
from bs4 import BeautifulSoup as bs
from selenium import webdriver


class Downloader():

    def __init__(self,songs):
        self.driver = webdriver.Chrome("chromedriver.exe")
        download_links = []
        for song in songs:
            q = "+".join(song).replace(' ', '+')
            search_link = "https://www.youtube.com/results?search_query="+q
            vid_link = "https://www.youtube.com"+self.get_video_link(search_link)
            download_links.append(vid_link)
            print(vid_link)

    def get_video_link(self,search_link):
        self.driver.get(search_link)
        time.sleep(1)
        req = self.driver.page_source
        cont = bs(req, 'html.parser')
        anch = cont.find('a',{"id":"video-title"})
        return anch['href']
