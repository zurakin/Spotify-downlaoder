import youtube_dl, time, os
from bs4 import BeautifulSoup as bs
from selenium import webdriver


class Downloader():

    def __init__(self,songs):
        self.driver = webdriver.Chrome("chromedriver.exe")
        download_links = []
        for song in songs:
            q = "+".join(song).replace(' ', '+')
            search_link = "https://www.youtube.com/results?search_query="+q+"+lyrics"
            try:
                vid_link = "https://www.youtube.com"+self.get_video_link(search_link)
            except:
                print(song,'skipped')
                continue
            download_links.append(vid_link)
        self.download(download_links)

    def get_video_link(self,search_link):
        self.driver.get(search_link)
        # time.sleep(1)
        req = self.driver.page_source
        cont = bs(req, 'html.parser')
        anch = cont.find('a',{"id":"video-title"})
        return anch['href']

    def download(self, download_links):
        ydl_opts = {'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',}]}
        try :
            os.chdir('downloads')
        except:
            os.mkdir('downloads')
            os.chdir('downloads')
        while True:
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(download_links)
                break
            except:
                print('downloading failed, retrying...')
                time.sleep(3)
