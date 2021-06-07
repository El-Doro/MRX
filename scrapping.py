#!/usr/bin/env python3
# coding:utf-8


# Import :
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
from collections import namedtuple
import re
from normalize import remove_special_characters
import requests
from pathlib import Path


Episode = namedtuple("Episode", ["url", "title"])

BASEURL = "http://rendezvousavecmrx.free.fr"

dossierSonsBruts = Path("./EpisodesBruts/")


"""
LES FONCTIONS
"""

# Fonction scraping qui récupère les url des épisodes à télécharger et les associe au titre dans un namedtuple
def scrape_episodes():
    episodes = []
    for link in soup.findAll("a", href=re.compile("\.mp3")):
        episode_url = urljoin(BASEURL, link.get("href"))
        title = remove_special_characters(link.find("img").get("title")) + ".mp3"
        episode = Episode(episode_url, title)
        episodes.append(episode)
    return episodes


# Fonction download


def download_episode(episode, destination_folder):
    file_stream = requests.get(episode.url, stream=True)
    with open(destination_folder / episode.title, "wb") as local_file:
        for data in file_stream:
            local_file.write(data)


"""
LE TRAITEMENT
"""
# Initier le parsing de la page par BeautifulSoup

link = urljoin(BASEURL, "page/liste.php")
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page, "html.parser")

# Récupérer les épisodes

episodes = scrape_episodes()

# Télécharger les épisodes
for episode in episodes:
    download_episode(episode, dossierSonsBruts)

"""

for episode in episodes:
	print(episode.url)
	destination_file = dossierSonsBruts / episode.title
	print(destination_file)
	file_stream = requests.get(episode.url, stream = True)
	with open(destination_file, 'wb') as local_file:
	    for data in file_stream:
		    local_file.write(data)

"""
