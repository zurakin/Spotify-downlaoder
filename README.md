# Spotify-downlaoder
 A tool for downloading spotify playlists. First songs are scraped from a playlist link. Then downloaded from youtube and converted to mp3 format.

# Installation
 1- Install python 3 and pip.
 2- Install the requirements using pip. To do that, open a command line in the program's folder and execute the command:
  pip install -r requirements.txt
 3- You need to have Chrome's web browser installed in your computer. After installing Chrome, download the 'Chrome WebDriver' that matches your version of Chrome. After downloading it, put it in the program's folder. Here's the download link: https://chromedriver.chromium.org/downloads
 4- To be able to download songs in mp3 format, you need to have 'ffmpeg codec' installed in your computer. To install it open a Power Shell and execute the following command:
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
 Now close the Power Shell and execute the following command in a command line:
  choco install ffmpeg

# Usage
  1- create a Spotify playlist containing all the songs you want to download.
  2- Right-click the playlist's name, Share, Copy Playlist Link.
  3- Open a command line in the program's folder and execute the command:
    py main.py {paste the playlist's link here}
    example: py main.py https://open.spotify.com/user/electropos%C3%A9/playlist/2oTrz1dYy2l970ptp4KZta?si=WInHtktVToOcXHb89trkFw
  4- The songs will automatically be downloaded and converted to mp3 format. Wait until you see the message : "Playlist downloaded successfully !". You can find the downloaded songs in the folder downloads in the program's directory.

# Notes
  If you have trouble downloading songs :
    *check your internet connection.
    *update youtube-dl: execute the following command in a command line:
      pip install -upgrade youtube-dl
