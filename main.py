from scraper import Miner
from youtube import Downloader

def main():
    m = Miner('https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=7HOF1owoRSWQb4UE4bSTdghttps://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=7HOF1owoRSWQb4UE4bSTdg')
    m.scrape()
    songs = m.titles_list
    d = Downloader(songs)


if __name__=="__main__":
    main()
