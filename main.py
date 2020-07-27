from scraper import Miner

m = Miner('https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=7HOF1owoRSWQb4UE4bSTdghttps://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=7HOF1owoRSWQb4UE4bSTdg')
m.scrape()
for e in m.titles_list:
    print(e)
