from bs4 import BeautifulSoup as bs
import requests



class Miner():
    def __init__(self, playlist_link):
        self.link = playlist_link
        self.titles_list = []
    def scrape(self):
        r = requests.get(self.link)
        c = r.content
        cont = bs(c, "html.parser")
        songs_list = cont.find('ol', {"class":"tracklist"})
        for s in songs_list:
            # title = s.find('div', {"class":"tracklis-name ellipsis-one-line"}).text.strip()
            title = s.find('span', {"class":"track-name"}).text.strip()
            # artist = s.find('div', {"class":"TrackListRow__artists ellipsis-one-line"}).text.strip()
            artist = s.find('span', {"class":"artists-albums"}).find('span').text.strip()

            self.titles_list.append([title, artist])
